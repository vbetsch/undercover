from src.core.Meta import Singleton
import json


class Service(metaclass=Singleton):
    def __init__(self):
        self.words = None
        self.rules = None
        self.files = {
            "words": 'words.json',
            "rules": 'rules.json'
        }

    @staticmethod
    def __load(path):
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def __dump(path, data):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_words(self):
        self.words = self.__load(self.files["words"])

    def compute_words(self, data):
        self.__dump(self.files["words"], data)

    def read_rules(self):
        self.rules = self.__load(self.files["rules"])

    def compute_rules(self, data):
        self.__dump(self.files["rules"], data)
