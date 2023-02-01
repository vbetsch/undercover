from src.core.Meta import Singleton


class Interactor(metaclass=Singleton):
    def __init__(self):
        self.error_code = "#####"
        self.warning_code = "-----"
        self.system_code = "$"
        self.dialog_code = "-"

    @staticmethod
    def call_input(text):
        return input(text)

    def call_int_input(self, text):
        return int(self.call_input(text))

    def call_error(self, content):
        print(self.error_code, content, self.error_code)

    def call_warning(self, content):
        print(self.warning_code, content, self.warning_code)

    def call_system(self, content):
        print(self.system_code, content)

    def call_dialog(self, content):
        print(self.dialog_code, content)
