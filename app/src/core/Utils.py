from app.src.core.Meta import Singleton


class Utils(metaclass=Singleton):
    def __init__(self):
        pass

    @staticmethod
    def exception(text):
        raise Exception(f"ERROR: {text}")

    @staticmethod
    def get_index_from_list(array, value):
        return array.index(value)

    @staticmethod
    def get_key_from_dict(array, value):
        for key, val in array.items():
            if val == value:
                return key
