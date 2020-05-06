import requests
from sennder.configs.config import GHIBLI_FILM_API, GHIBLI_PEOPLE_API


class GhibliApi:

    @staticmethod
    def get_films():
        """
        Retrieve films data from ghibli api
        :return: dict or list
        """
        resp = requests.get(url=GHIBLI_FILM_API, params={})
        return resp.json()

    @staticmethod
    def get_people():
        """
        Retrieve people data from ghibli api
        :return: dict or list
        """
        resp = requests.get(url=GHIBLI_PEOPLE_API, params={})
        return resp.json()
