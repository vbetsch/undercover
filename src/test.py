from src.core.Game import Game
from src.core.Interactor import Interactor
from src.core.Service import Service


def test_game():
    print(Service().config["lang"])
    with Game() as game:
        game.sum_players = 5
        for index in range(1, game.sum_players + 1):
            game.players[f"{Interactor().trad('game_config', '_player').capitalize()}{index}"] = None
        game.run()


test_game()
