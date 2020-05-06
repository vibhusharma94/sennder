import unittest
from sennder.app import create_app
from sennder.resources.api import Movies
from sennder.handlers import MovieHandler
from sennder.handlers import BaseHandler
from sennder.exceptions import HandlerClassNotDefined


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def test_successful_movies(self):
        response = self.app.get('/movies', headers={"Content-Type": "application/json"})
        self.assertEqual(list, type(response.json))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        pass


class BaseResourceTestCase(unittest.TestCase):

    def setUp(self):
        self.resource = Movies()

    def test_get_handler_success(self):
        handler_object = self.resource.get_handler()
        self.assertIsInstance(handler_object, MovieHandler)
        expression = issubclass(handler_object.__class__, BaseHandler)
        self.assertTrue(expression)

    def test_get_handler_raise_exception(self):
        self.resource.handler_class = None
        self.assertRaises(HandlerClassNotDefined, self.resource.get_handler)

    def tearDown(self):
        pass
