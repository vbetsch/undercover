from src.core.Meta import Singleton
from src.core.Service import Service


class Interactor(metaclass=Singleton):
    def __init__(self):
        self.error_code = "#####"
        self.warning_code = "-----"
        self.system_code = "|"
        self.dialog_code = "->"
        self.progress = "..."

    @staticmethod
    def trad(group, key):
        return Service().dict[group][key]

    def call_input(self, text):
        return input(f"{self.dialog_code} {text}")

    def call_int_input(self, text):
        return int(self.call_input(text))

    def call_error(self, content):
        print(f"{self.error_code} [{Interactor().trad('messages', '_error').upper()}] {content} {self.error_code}")

    def call_warning(self, content):
        print(f"{self.warning_code} [{Interactor().trad('messages', '_warning').upper()}] {content} {self.warning_code}")

    def call_system(self, content):
        print(self.system_code, content)
