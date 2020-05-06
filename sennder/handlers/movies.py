from collections import defaultdict

from sennder.tasks import GhibliApi
from sennder.exceptions import RedisKeyNotFound
from sennder.handlers import BaseHandler
from sennder.repository import MovieRepo, PeopleRepo


class MovieHandler(BaseHandler):

    def handle(self):
        movie_repo = MovieRepo()
        people_repo = PeopleRepo()
        try:
            movies = movie_repo.get_movies()
            people = people_repo.get_people()
        except RedisKeyNotFound:  # data not exist or expired ( 60 sec )
            # Fetch latest data
            api = GhibliApi()
            movies = api.get_films()
            people = api.get_people()

            # save data to Redis
            movie_repo.add_movies(movies)
            people_repo.add_people(people)

        # combine cast with their movies
        data = self._combine(movies, people)
        return data

    @staticmethod
    def _combine(movies, people):
        film_cast = defaultdict(list)
        for person in people:
            try:
                film_id = person["films"][0].split("/")[-1]
            except (KeyError, IndexError):
                # Return data from api is corrupted so better to skip
                continue

            film_cast[film_id].append(person)

        for m in movies:
            m["people"] = film_cast.get(m["id"], [])

        return movies
