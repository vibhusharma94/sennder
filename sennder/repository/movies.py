import json
from sennder.repository import BaseRepo


class MovieRepo(BaseRepo):

    def get_movies(self):
        """
        :return: List of dict
        """
        data_str = self._get("movies")
        return json.loads(data_str)

    def add_movies(self, items):
        """
        :param items:
        :return: nothing
        """
        data_str = json.dumps(items)
        self._set("movies", data_str)


class PeopleRepo(BaseRepo):

    def get_people(self):
        """
        :return: List of dict
        """
        data_str = self._get("people")
        return json.loads(data_str)

    def add_people(self, items):
        """
        :param items:
        :return: nothing
        """
        data_str = json.dumps(items)
        self._set("people", data_str)
