#!/usr/bin/python

from src.core.Game import Game


def init():
    # Service().clear_games()
    pass


def main():
    with Game() as game:
        game.run()


if __name__ == '__main__':
    init()
    main()
