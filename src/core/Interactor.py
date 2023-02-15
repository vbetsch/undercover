from src.core.Meta import Singleton
from src.core.Service import Service
from src.core.Utils import Utils


class Interactor(metaclass=Singleton):
    def __init__(self):
        self.error_code = "#####"
        self.warning_code = "-----"
        self.system_code = "|"
        self.dialog_code = "->"
        self.progress = "..."

    @staticmethod
    def trad(group, key):
        to_return = Service().dict[group][key]
        if not to_return:
            return Utils().exception(f"Translation is missing on {Service().get_lang()} for key {key} in group {group}")
        return to_return

    def call_input(self, text):
        return input(f"{self.dialog_code} {text}")

    def call_int_input(self, text):
        return int(self.call_input(text))

    def call_system(self, content):
        print(self.system_code, content)

    def error(self, content):
        print(f"{self.error_code} [{self.trad('messages', '_error').upper()}] {content} {self.error_code}")

    def warning(self, content):
        print(f"{self.warning_code} [{self.trad('messages', '_warning').upper()}] {content} {self.warning_code}")
