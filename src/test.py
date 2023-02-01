from src.core.Game import Game
from src.core.Interactor import Interactor
from src.core.Service import Service


def test_game():
    print(Service().config["lang"])
    print(Interactor()._("_example"))
    with Game() as game:
        game.sum_players = 5
        for index in range(1, game.sum_players + 1):
            game.players[f"{Interactor()._('_player')}{index}"] = None
        game.run()


test_game()
