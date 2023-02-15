from src.core.Interactor import Interactor
from src.core.Service import Service
from src.core.Utils import Utils


class Game:
    def __init__(self):
        # --------------------------- DATA VARIABLES ---------------------------
        self.players = Service().rules["PLAYERS"]["ROLE_PLAYERS"]
        self.white_players = Service().rules["PLAYERS"]["WHITE_PLAYERS"]
        self.undercover_players = Service().rules["PLAYERS"]["UNDERCOVER_PLAYERS"]
        self.civilian_players = Service().rules["PLAYERS"]["CIVILIAN_PLAYERS"]
        self.roles = Service().rules["ROLES"]

        # --------------------------- RULES VARIABLES ---------------------------
        self.sum_players = 0

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_value:
            self.close()
            Utils().exception(exc_value)
        self.save_state()
        self.close()
        return self

    def load(self):
        Service().read_games()
        game = Service().find_game(Service().config["last_game"])
        if game:
            Service().rules = game["rules"]
            Service().words = game["words"]
            Interactor().call_system(f"{Interactor().trad('game_config', '_game_found')}{Interactor().progress}")
        else:
            Interactor().warning(f"{Interactor().trad('game_config', '_game_not_found')}")
            self.config()

    def save_state(self):
        Service().compute_rules()
        Service().compute_words()
        Service().games.append({
            "id": self.__hash__(),
            "default": Service().get_default(),
            "rules": Service().rules,
            "words": Service().words
        })
        Interactor().call_system(f"{Interactor().trad('game_config', '_game_saved')}")

    def close(self):
        Interactor().call_system(f"{Interactor().trad('game_config', '_game_closed')}{Interactor().progress}")
        Service().compute_games()
        Service().update_last_game(self.__hash__())
        Service().compute_config()

    def config(self):
        Interactor().call_system(f"{Interactor().trad('game_config', '_new_game')}")
        # --------------------------- PLAYERS ---------------------------
        self.sum_players = Interactor().call_int_input(
            f"{Interactor().trad('game_config', '_number_of_players').capitalize()} : ")

        for index in range(1, self.sum_players + 1):
            self.players[Interactor().call_input(
                f"{Interactor().trad('game_config', '_name_of_player').capitalize()} ({index}) : ")] = None

        Service().compute_rules()
    
    @staticmethod
    def run():
        Interactor().call_system(
            f"{Interactor().trad('actions', '_running').capitalize()}{Interactor().progress}")
        print(Service().rules)
        print(Service().words)
