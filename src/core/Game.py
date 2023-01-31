from src.core.Service import Service


class Game:
    def __init__(self):                        # def __init__(self, config):
        print("Creating", self)
        Service().read_default()
        Service().read_words()

        # --------------------------- DATA VARIABLES ---------------------------
        self.players = Service().rules["PLAYERS"]["ROLE_PLAYERS"]
        self.white_players = Service().rules["PLAYERS"]["WHITE_PLAYERS"]
        self.undercover_players = Service().rules["PLAYERS"]["UNDERCOVER_PLAYERS"]
        self.civilian_players = Service().rules["PLAYERS"]["CIVILIAN_PLAYERS"]
        self.roles = Service().rules["ROLES"]

        # --------------------------- RULES VARIABLES ---------------------------
        self.sum_players = 0

    def __enter__(self):
        # self.load()
        print("Open", self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # self.save_state()
        # self.close()
        print("Exit", self)
        return self

    def run(self):
        print("Running", self)
        print(Service().rules)
        print(Service().words)

        print(self.sum_players)
