from app.src.core.Meta import Singleton
import json


class Utils(metaclass=Singleton):
    def __init__(self):
        pass

    @staticmethod
    def load(path):
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def dump(path, data):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def exception(text):
        raise Exception(f"'{text}'")

    @staticmethod
    def get_index_from_list(array, value):
        return array.index(value)

    @staticmethod
    def get_key_from_dict(array, value):
        for key, val in array.items():
            if val == value:
                return key
