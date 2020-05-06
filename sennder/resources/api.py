from http import HTTPStatus
from sennder.handlers import MovieHandler
from sennder.resources import BaseResource


class Movies(BaseResource):
    handler_class = MovieHandler

    def get(self):
        """
        :return: list of movies
        """
        handler = self.get_handler()
        data = handler.handle()
        return data, HTTPStatus.OK
