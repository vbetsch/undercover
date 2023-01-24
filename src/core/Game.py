from src.core.Service import Service


class Game:
    def __init__(self):                        # def __init__(self, config):
        print("Creating", self)
        Service().read_words()
        self.WORDS = Service().words

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
        return self
