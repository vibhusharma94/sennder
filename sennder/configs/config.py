from os import environ

REDIS_HOST = environ.get("REDIS_HOST", "0.0.0.0")
REDIS_PORT = environ.get("REDIS_PORT", 6379)
REDIS_DB = environ.get("REDIS_DB", 1)
REDIS_DATA_EXPIRE = 60

BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(
    host=REDIS_HOST, port=str(REDIS_PORT)))
CELERY_RESULT_BACKEND = BROKER_URL
GHIBLI_FILM_API = "https://ghibliapi.herokuapp.com/films"
GHIBLI_PEOPLE_API = "https://ghibliapi.herokuapp.com/people"

REDIS_PUBSUB_DB = 2
PUBSUB_CHANNEL = "movies"