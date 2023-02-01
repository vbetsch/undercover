from src.core.Meta import Singleton


class Interactor(metaclass=Singleton):
    def __init__(self):
        self.error_code = "#####"
        self.warning_code = "-----"
        self.system_code = "$"
        self.dialog_code = "-"

    @staticmethod
    def callInput(text):
        return input(text)

    def callIntInput(self, text):
        return int(self.callInput(text))

    def callError(self, content):
        print(self.error_code, content, self.error_code)

    def callWarning(self, content):
        print(self.warning_code, content, self.warning_code)

    def callSystem(self, content):
        print(self.system_code, content)

    def callDialog(self, content):
        print(self.dialog_code, content)
