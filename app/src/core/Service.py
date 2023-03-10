from app.src.core.Meta import Singleton
from app.src.core.Utils import Utils


class Service(metaclass=Singleton):
    def __init__(self):
        self.games = []
        self.config_path = 'config.json'
        self.config = Utils().load(self.config_path)
        self.words = Utils().load(self.config["constants"]["sources"]["words"])
        self.rules = Utils().load(self.config["constants"]["sources"]["default"])
        self.langs = {
            "fr": f"{self.config['lang_dir']}/fr.json",
            "en": f"{self.config['lang_dir']}/en.json"
        }
        self.dict = Utils().load(self.langs[self.config["lang"]])

    def compute_config(self):
        Utils().dump(self.config_path, self.config)

    def get_lang(self):
        return self.config["lang"]

    def update_lang(self, lang):
        self.dict = Utils().load(self.langs[lang])

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
        self.games = Utils().load(self.config["constants"]["sources"]["games"])

    def compute_games(self):
        Utils().dump(self.config["constants"]["sources"]["games"], self.games)

    def clear_games(self):
        self.games = []
        self.words = []
        self.rules = []
        self.compute_games()

    def get_default(self):
        return Utils().load(self.config["constants"]["sources"]["default"])

    def read_rules(self):
        self.rules = Utils().load(self.config["constants"]["sources"]["rules"])

    def compute_rules(self):
        Utils().dump(self.config["constants"]["sources"]["rules"], self.rules)

    def read_words(self):
        self.words = Utils().load(self.config["constants"]["sources"]["words"])

    def compute_words(self):
        Utils().dump(self.config["constants"]["sources"]["words"], self.words)
