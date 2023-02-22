import json

from app.src.core.Meta import Singleton


class Service(metaclass=Singleton):
    def __init__(self):
        self.games = []
        self.config_path = 'config.json'
        self.config = self.__load(self.config_path)
        self.words = self.__load(self.config["constants"]["sources"]["words"])
        self.rules = self.__load(self.config["constants"]["sources"]["default"])
        self.langs = {
            "fr": f"{self.config['lang_dir']}/fr.json",
            "en": f"{self.config['lang_dir']}/en.json"
        }
        self.dict = self.__load(self.langs[self.config["lang"]])

    @staticmethod
    def __load(path):
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def __dump(path, data):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def compute_config(self):
        self.__dump(self.config_path, self.config)

    def get_lang(self):
        return self.config["lang"]

    def update_lang(self, lang):
        self.dict = self.__load(self.langs[lang])

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
        self.games = self.__load(self.config["constants"]["sources"]["games"])

    def compute_games(self):
        self.__dump(self.config["constants"]["sources"]["games"], self.games)

    def clear_games(self):
        self.games = []
        self.words = []
        self.rules = []
        self.compute_games()

    def get_default(self):
        return self.__load(self.config["constants"]["sources"]["default"])

    def read_rules(self):
        self.rules = self.__load(self.config["constants"]["sources"]["rules"])

    def compute_rules(self):
        self.__dump(self.config["constants"]["sources"]["rules"], self.rules)

    def read_words(self):
        self.words = self.__load(self.config["constants"]["sources"]["words"])

    def compute_words(self):
        self.__dump(self.config["constants"]["sources"]["words"], self.words)
