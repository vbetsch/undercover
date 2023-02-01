from src.core.Meta import Singleton
import json


class Service(metaclass=Singleton):
    def __init__(self):
        self.config = None
        self.words = None
        self.rules = None
        self.files = {
            "config": 'config.json',
            "words": 'data/words.json',
            "default": 'data/default.json',
            "rules": 'data/rules.json'
        }

    @staticmethod
    def __load(path):
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def __dump(path, data):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def read_config(self):
        self.config = self.__load(self.files["config"])
    
    def read_default(self):
        self.rules = self.__load(self.files["default"])

    def read_words(self):
        self.words = self.__load(self.files["words"])

    def compute_words(self, data):
        self.__dump(self.files["words"], data)

    def read_rules(self):
        self.rules = self.__load(self.files["rules"])

    def compute_rules(self):
        self.__dump(self.files["rules"], self.rules)
