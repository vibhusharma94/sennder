from sennder.storage import DataStore
from sennder.configs.config import REDIS_DATA_EXPIRE


class BaseRepo:
    """
    Abstraction layer on top of Redis.
    It's completely optional but it does help decoupled database query from Handler hence better testability.
    """

    def __init__(self):
        self._store = DataStore()

    def _get(self, key):
        """
        Retrieve value from database
        :param key:
        :return: string
        """
        return self._store.get(key)

    def _set(self, key, value):
        """
        Insert value to database.
        :param key:
        :param value:
        :return: nothing
        """
        self._store.set(key, value, expire=REDIS_DATA_EXPIRE)
