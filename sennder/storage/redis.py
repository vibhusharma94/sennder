import redis
from sennder.exceptions import RedisKeyNotFound
from sennder.db import get_db


class DataStore:
    """
    Abstraction layer on top of redis module.
    """

    def __init__(self):
        """
        Connect to redis server.
        """
        try:
            self.db = get_db()
        except RuntimeError:  # Would fail if class is instantiated outside of app context
            self.db = redis.StrictRedis()

    def get(self, key):
        """
        Retrieve value using key
        :param key: redis key
        :return: returns string
        "raises: raise exception if redis key does not exist
        """
        json_str = self.db.get(key)
        if not json_str:
            raise RedisKeyNotFound("Key does not exist.")
        return json_str

    def set(self, key, data={}, expire=None):
        """
        Insert value in redis
        :param key:
        :param data:
        :param expire:
        :return: returns nothing
        """
        self.db.set(key, data, ex=expire)
