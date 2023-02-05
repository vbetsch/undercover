from src.core.Inspector import Inspector
from src.core.Interactor import Interactor


class Menu:
    def __init__(self, mode, title, *entries):
        self.mode = mode
        self.title = title.upper()
        self.options = {}
        self.entries = list(entries)
        self.compute_options()

    def compute_options(self):
        match self.mode:
            case "first_letters":
                for entry in self.entries:
                    self.options[entry[0].lower()] = entry.capitalize()
            case "numbers":
                for index in range(0, len(self.entries)):
                    self.options[index + 1] = self.entries[index].capitalize()
            case _:
                Inspector().exception(Interactor().trad("menu", "_menu_mode_not_found"))

    def show(self):
        result = f"--------------- {self.title} ---------------\n"
        for opt in self.options:
            result += f"({opt}) {self.options[opt]}\n"
        print(result)

    def add_options(self, *entries):
        self.entries.extend(list(entries))
        self.compute_options()

    # TODO: def update_option(self, index, option)
    # TODO: def insert_option(self, position, option)
