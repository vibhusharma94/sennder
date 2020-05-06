import json
from abc import abstractmethod, ABC


class BaseHandler(ABC):

    @abstractmethod
    def handle(self):
        """
        Business logic goes here. Every class must implement this method.
        :return:
        """
        pass

    @staticmethod
    def serialize(data_dict):
        """
        :param data_dict:
        :return: serialized json string
        """
        data_str = json.dumps(data_dict)
        return data_str

    @staticmethod
    def deserialize(data_str):
        """
        :param data_str:
        :return:
        """
        data_dict = json.loads(data_str)
        return data_dict
