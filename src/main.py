from src.Game import Game


def main():
    with Game() as game:
        game.run()


if __name__ == '__main__':
    main()
