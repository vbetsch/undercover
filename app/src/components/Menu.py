from app.src.core.Inspector import Inspector
from app.src.core.Interactor import Interactor
from app.src.core.Utils import Utils


class Menu:
    def __init__(self, mode, title, *entries):
        self.mode = mode
        self.title = title
        self.options = {}
        self.entries = []
        for entry in entries:
            self.entries.append(entry.lower())
        self.compute_options()

    def compute_options(self):
        self.options = {}
        match self.mode:
            case "first_letters":
                if Inspector().same_first_letter(self.entries):
                    Utils().exception("Some options start with same letter")
                for entry in self.entries:
                    self.options[entry[0].lower()] = entry.lower()
            case "numbers":
                for index in range(0, len(self.entries)):
                    self.options[index + 1] = self.entries[index].lower()
            case _:
                Utils().exception(Interactor().trad("menu", "_menu_mode_not_found"))

    def text(self):
        result = f"--------------- {self.title.upper()} ---------------"
        for opt in self.options:
            result += f"\n({opt}) {self.options[opt].capitalize()}"
        return result

    def show(self):
        print(self.text)

    def add_options(self, *entries):
        for entry in entries:
            self.entries.append(entry.lower())
        self.compute_options()

    def insert_options(self, **options):
        for key, value in options.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            self.entries.insert(self.entries.index(self.options[key]), value.lower())
        self.compute_options()

    def update_option(self, opt, entry):
        opt = opt.lower()
        if not self.exist_option(opt):
            Utils().exception("Option not found")
        self.entries[Utils().get_index_from_list(self.entries, opt)] = entry.lower()
        self.compute_options()

    def update_option_by_index(self, index, entry):
        if not self.exist_option_by_index(index):
            Utils().exception("Index not found")
        self.entries[index - 1] = entry.lower()
        self.compute_options()

    def update_options_by_key(self, **kwargs):
        for key, value in kwargs.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            self.update_option(self.options[key], value.lower())

    def delete_option(self, opt):
        opt = opt.lower()
        if not self.exist_option(opt):
            Utils().exception("Option not found")
        if self.exist_option(opt):
            self.entries.pop(Utils().get_index_from_list(self.entries, opt))
            self.compute_options()

    def delete_option_by_index(self, index):
        if not self.exist_option_by_index(index):
            Utils().exception("Index not found")
        self.entries.pop(Utils().get_index_from_list(self.entries, self.entries[index - 1]))
        self.compute_options()

    def delete_options_by_key(self, *args):
        for arg in args:
            arg = arg.lower()
            if not self.exist_key(arg):
                Utils().exception(f"Key {arg} not found")
            if Inspector().element_in_list(arg, self.options.keys()):
                self.entries.pop(Utils().get_index_from_list(self.entries, self.options[arg]))
                self.compute_options()

    def exist_key(self, key):
        if Inspector().element_in_list(key.lower(), self.options.keys()):
            return True
        else:
            return False

    def exist_option(self, opt):
        if Inspector().element_in_list(opt.lower(), self.entries):
            return True
        else:
            return False

    def exist_option_by_index(self, index):
        if index < 1 or index > len(self.entries):
            return False
        else:
            return True

    def exist_one_option(self, options):
        for opt in options:
            opt = opt.lower()
            if self.exist_option(opt):
                return True
        return False

    def exist_all_options(self, options):
        for opt in options:
            opt = opt.lower()
            if not self.exist_option(opt):
                return False
        return True
