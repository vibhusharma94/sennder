import json
import redis
import asyncio
import aiohttp
import logging
from aiohttp import web

from sennder.configs.config import REDIS_PUBSUB_DB, PUBSUB_CHANNEL

log = logging.getLogger(__name__)
GlobalAPP = None


class IoHandler:

    def __init__(self):
        self.p = None

    @staticmethod
    async def handle(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        request.app['connections'].add(ws)
        try:
            async for msg in ws:
                print(msg.type)
                if msg.type == aiohttp.WSMsgType.TEXT:
                    pass
        finally:
            request.app['connections'].discard(ws)
        return ws

    def subscribe(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=REDIS_PUBSUB_DB)
        self.p = r.pubsub()
        self.p.subscribe(PUBSUB_CHANNEL)

    def get_message(self):
        message = self.p.get_message()
        try:
            return json.loads(message["data"])
        except (KeyError, TypeError, OverflowError):
            log.info("Failed to serialize data")
            return None

    async def message_dispatcher(self):
        while True:
            data = self.get_message()
            if data:
                for client in GlobalAPP['connections']:
                    await client.send_json(
                        {'action': 'sent', 'msg': data})
            await asyncio.sleep(5)


async def setup_server(loop, address, port):
    global GlobalAPP
    GlobalAPP = app = web.Application(loop=loop)
    app.router.add_route('GET', '/ws', IoHandler.handle)
    app['connections'] = set()
    return await loop.create_server(app.make_handler(), address, port)


def main():
    io = IoHandler()
    io.subscribe()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run_coroutine_threadsafe(setup_server(loop, 'localhost', 8080), loop)
    asyncio.run_coroutine_threadsafe(io.message_dispatcher(), loop)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        log.debug("Shutting Down");
        loop.close()


if __name__ == '__main__':
    main()
