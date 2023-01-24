from src.core.Service import Service


class Game:
    def __init__(self):                        # def __init__(self, config):
        print("Creating", self)
        Service().read_default()
        Service().read_words()

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

        # --------------------------- DATA VARIABLES ---------------------------
        players = Service().rules["PLAYERS"]["ROLE_PLAYERS"]
        white_players = Service().rules["PLAYERS"]["WHITE_PLAYERS"]
        undercover_players = Service().rules["PLAYERS"]["UNDERCOVER_PLAYERS"]
        civilian_players = Service().rules["PLAYERS"]["CIVILIAN_PLAYERS"]
        roles = Service().rules["ROLES"]

        # --------------------------- PLAYERS ---------------------------
        sum_players = 5  # sum_players = int(input("Players : "))

        for index in range(1, sum_players + 1):
            players[f"Player{index}"] = None  # PLAYERS[input(f"Name of player ({index}) : ")] = None
        return self
