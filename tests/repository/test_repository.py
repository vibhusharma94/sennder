import unittest
from sennder.repository import MovieRepo, PeopleRepo


class MovieTestCase(unittest.TestCase):

    def setUp(self):
        self.repo = MovieRepo()

    def test_get_movies(self):
        items = self.repo.get_movies()
        self.assertIsInstance(items, list)
        self.assertNotEqual(len(items), 0)

    def test_add_movies(self):
        items = [{"name": "Godfather"}]
        self.repo.add_movies(items)
        movies = self.repo.get_movies()
        self.assertEqual(movies, items)


class PeopleTestCase(unittest.TestCase):

    def setUp(self):
        self.repo = PeopleRepo()

    def test_get_people(self):
        items = self.repo.get_people()
        self.assertIsInstance(items, list)
        self.assertNotEqual(len(items), 0)

    def test_add_people(self):
        items = [{"name": "Benedict Cumberbatch"}]
        self.repo.add_people(items)
        people = self.repo.get_people()
        self.assertEqual(people, items)
