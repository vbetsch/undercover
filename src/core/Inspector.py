from src.core.Interactor import Interactor
from src.core.Meta import Singleton


class Inspector(metaclass=Singleton):
    def __init__(self):
        pass

    @staticmethod
    def exception(text):
        raise Exception(f"{Interactor().error_code} [{Interactor().trad('messages', '_error').upper()}] {text} {Interactor().error_code}")

    @staticmethod
    def error(text):
        Interactor().call_error(text)

    @staticmethod
    def warning(text):
        Interactor().call_warning(text)
