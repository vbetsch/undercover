from src.core.Game import Game


def test_game():
    with Game() as game:
        game.sum_players = 5
        game.run()


test_game()
