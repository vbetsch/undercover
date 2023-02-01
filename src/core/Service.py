from src.core.Meta import Singleton
import json


class Service(metaclass=Singleton):
    def __init__(self):
        self.files = {
            "config": 'config.json',
            "words": 'data/words.json',
            "default": 'data/default.json',
            "rules": 'data/rules.json',
            "langs": {
                "fr": 'lang/fr.json',
                "en": 'lang/en.json'
            }
        }
        self.config = self.__load(self.files["config"])
        self.words = self.__load(self.files["words"])
        self.rules = self.__load(self.files["default"])
        self.dict = self.__load(self.files["langs"][self.config["lang"]])
    
    
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
    
    
    def compute_rules(self):
        self.__dump(self.files["rules"], self.rules)
    
    
    def change_lang(self, lang):
        self.dict = self.__load(self.files["langs"][lang])
