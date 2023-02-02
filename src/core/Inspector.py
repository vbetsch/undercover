from src.core.Interactor import Interactor
from src.core.Meta import Singleton


class Inspector(metaclass=Singleton):
    def __init__(self):
        pass

    @staticmethod
    def exception(text):
        raise Exception(text)

    @staticmethod
    def error(text):
        Interactor().call_error(text)

    @staticmethod
    def warning(text):
        Interactor().call_warning(text)
