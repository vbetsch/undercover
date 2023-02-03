import json

from src.core.Meta import Singleton


class Service(metaclass=Singleton):
    def __init__(self):
        self.games = []
        self.files = {
            "config": 'config.json',
            "default": 'data/default.json',
            "rules": 'data/rules.json',
            "words": 'data/words.json',
            "games": 'data/games.json',
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
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def __dump(path, data):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def compute_config(self):
        self.__dump(self.files["config"], self.config)

    def update_lang(self, lang):
        self.dict = self.__load(self.files["langs"][lang])

    def update_last_game(self, value):
        self.config["last_game"] = value

    def find_game(self, _id):
        index = 0
        while index < len(self.games):
            if self.games[index]["id"] == _id:
                return self.games[index]
            index += 1
        return None

    def read_games(self):
        self.games = self.__load(self.files["games"])

    def compute_games(self):
        self.__dump(self.files["games"], self.games)

    def clear_games(self):
        self.games = []
        self.words = []
        self.rules = []
        self.compute_games()

    def get_default(self):
        return self.__load(self.files["default"])

    def read_rules(self):
        self.rules = self.__load(self.files["rules"])

    def compute_rules(self):
        self.__dump(self.files["rules"], self.rules)

    def read_words(self):
        self.words = self.__load(self.files["words"])

    def compute_words(self):
        self.__dump(self.files["words"], self.words)
