from src.core.Game import Game
from src.core.Interactor import Interactor
from src.core.Service import Service


def init():
    pass


def main():
    init()
    with Game() as game:
        game.config()
        game.run()


if __name__ == '__main__':
    main()
