import json
import celery
import redis
from sennder.tasks.api import GhibliApi
from sennder.repository import MovieRepo, PeopleRepo
from sennder.configs.config import REDIS_PUBSUB_DB, PUBSUB_CHANNEL


@celery.task()
def fetch_movie_data():
    """
    This task will run every minute to fetch latest movies data and store in Redis.
    :return: nothing
    """
    logger = fetch_movie_data.get_logger()
    logger.info("Fetching movies and people data....")
    api = GhibliApi()
    movies = api.get_films()
    people = api.get_people()
    MovieRepo().add_movies(movies)
    PeopleRepo().add_people(people)
    publisher(movies)


def publisher(data):
    r = redis.StrictRedis(host='localhost', port=6379, db=REDIS_PUBSUB_DB)
    r.publish(PUBSUB_CHANNEL, json.dumps(data))
