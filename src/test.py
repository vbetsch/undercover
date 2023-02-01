from src.core.Game import Game


def test_game():
    with Game() as game:
        game.sum_players = 5
        for index in range(1, game.sum_players + 1):
            game.players[f"Player{index}"] = None
        game.run()


test_game()
