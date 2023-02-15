from app.src.core.Inspector import Inspector
from app.src.core.Interactor import Interactor
from app.src.core.Utils import Utils


class Menu:
    def __init__(self, mode, title, *entries):
        self.mode = mode
        self.title = title
        self.options = {}
        self.entries = list(entries)
        self.compute_options()

    def compute_options(self):
        self.options = {}
        match self.mode:
            case "first_letters":
                if Inspector().same_first_letter(self.entries):
                    Utils().exception("Some options start with same letter")
                for entry in self.entries:
                    self.options[entry[0]] = entry
            case "numbers":
                for index in range(0, len(self.entries)):
                    self.options[index + 1] = self.entries[index]
            case _:
                Utils().exception(Interactor().trad("menu", "_menu_mode_not_found"))

    def show(self):
        result = f"--------------- {self.title.upper()} ---------------"
        for opt in self.options:
            result += f"\n({opt.lower()}) {self.options[opt].capitalize()}"
        print(result)

    def add_options(self, *entries):
        self.entries.extend(list(entries))
        self.compute_options()

    def insert_options(self, **options):
        for key, value in options.items():
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            self.entries.insert(self.entries.index(self.options[key]), value)
        self.compute_options()

    def update_option(self, opt, entry):
        if not self.exist_option(opt):
            Utils().exception("Option not found")
        self.entries[Utils().get_index_from_list(self.entries, opt)] = entry
        self.compute_options()

    def update_option_by_index(self, index, entry):
        if not self.exist_option_by_index(index):
            Utils().exception("Index not found")
        self.entries[index - 1] = entry
        self.compute_options()

    def update_options_by_key(self, **kwargs):
        for key, value in kwargs.items():
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            self.update_option(self.options[key], value)

    def delete_option(self, opt):
        if not self.exist_option(opt):
            Utils().exception("Option not found")
        alternatives = [opt.upper(), opt.lower(), opt.capitalize()]
        for alt in alternatives:
            if self.exist_option(alt):
                self.entries.pop(Utils().get_index_from_list(self.entries, alt))
                self.compute_options()

    def delete_option_by_index(self, index):
        if not self.exist_option_by_index(index):
            Utils().exception("Index not found")
        self.entries.pop(Utils().get_index_from_list(self.entries, self.entries[index - 1]))
        self.compute_options()

    def delete_options_by_key(self, *args):
        for arg in args:
            if not self.exist_key(arg):
                Utils().exception(f"Key {arg} not found")
            alternatives = [arg.upper(), arg.lower()]
            for alt in alternatives:
                if Inspector().element_in_list(alt, self.options.keys()):
                    self.entries.pop(Utils().get_index_from_list(self.entries, self.options[alt]))
                    self.compute_options()

    def exist_key(self, key):
        if Inspector().element_in_list(key, self.options.keys()):
            return True
        else:
            return False

    def exist_option(self, opt):
        if Inspector().element_in_list(opt, self.entries):
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
            alternatives = [opt.upper(), opt.lower(), opt.capitalize()]
            for alt in alternatives:
                if self.exist_option(alt):
                    return True
        return False

    def exist_all_options(self, options):
        for opt in options:
            alternatives = [opt.upper(), opt.lower(), opt.capitalize()]
            for alt in alternatives:
                if not self.exist_option(alt):
                    return False
        return True
