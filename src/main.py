from src.core.Game import Game
from src.core.Service import Service


def init():
    Service().read_config()


def main():
    init()
    with Game() as game:
        game.config()
        game.run()


if __name__ == '__main__':
    main()
