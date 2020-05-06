import inspect
from flask_restful import Resource
from sennder.handlers import BaseHandler
from sennder.exceptions import HandlerClassNotDefined


class BaseResource(Resource):
    handler_class = None

    def get_handler(self):
        """
        :return: returns handler object
        :raises: raise exception if handler_class attribute is not correctly defined.
        """
        if inspect.isclass(self.handler_class) and issubclass(self.handler_class, BaseHandler):
            return self.handler_class()
        else:
            raise HandlerClassNotDefined("Handler class not defined.")
