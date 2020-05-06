import unittest

from sennder.storage import DataStore
from sennder.exceptions import RedisKeyNotFound


class StorageTestCase(unittest.TestCase):

    def setUp(self):
        self.store = DataStore()
        self.store.db.set("movie", "Inception")

    def test_get_success(self):
        value = self.store.get("movie")
        self.assertIsInstance(value, bytes)
        self.assertEqual(value, bytes("Inception", "utf-8"))

    def test_set_success(self):
        self.store.set("movie", "Avenger")
        value = self.store.db.get("movie")
        self.assertIsInstance(value, bytes)
        self.assertEqual(value, bytes("Avenger", "utf-8"))

    def test_get_failed(self):
        """
        Try to get Unknown key so should raise RedisKeyNotFound exception.
        """
        self.assertRaises(RedisKeyNotFound, self.store.get, "unknown_key")
