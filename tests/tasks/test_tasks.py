import unittest
from sennder.tasks import GhibliApi


class TaskTestCase(unittest.TestCase):

    def test_get_movies_success(self):
        api = GhibliApi()
        items = api.get_films()
        self.assertIsInstance(items, list)
        self.assertNotEqual(len(items), 0)

    def test_get_people_success(self):
        api = GhibliApi()
        items = api.get_people()
        self.assertIsInstance(items, list)
        self.assertNotEqual(len(items), 0)
