import unittest
from sennder.handlers import MovieHandler


class HandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.handler = MovieHandler()

    def test_execute_success(self):
        items = self.handler.handle()
        self.assertIsInstance(items, list)
        self.assertNotEqual(len(items), 0)

    def test_serialize_success(self):
        data = [{"name": "Vibhu"}]
        value = self.handler.serialize(data)
        self.assertEqual(type(value), str)

    def test_serialize_failed(self):
        data = type("Random", (), {})()
        self.assertRaises(TypeError, self.handler.serialize, data)

    def test_deserialize_success(self):
        data = '[{"name": "Vibhu"}]'
        value = self.handler.deserialize(data)
        self.assertEqual(type(value), list)

    def test_deserialize_failed(self):
        data = {}
        self.assertRaises(TypeError, self.handler.deserialize, data)
