from src.core.Inspector import Inspector
from src.core.Interactor import Interactor
from src.core.Utils import Utils


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
        self.one_option_already_exist(entries)
        self.entries.extend(list(entries))
        self.compute_options()

    def insert_options(self, *options):
        self.one_option_already_exist(options)
        for opt in options:
            self.entries.insert(opt[0] - 1, opt[1])
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

    # TODO: multiple options
    def update_option_by_key(self, key, entry):
        self.update_option(self.options[key], entry)

    def delete_option(self, opt):
        alternatives = [opt.upper(), opt.lower(), opt.capitalize()]
        for alt in alternatives:
            if self.exist_option(alt):
                print("Success")
                self.entries.pop(Utils().get_index_from_list(self.entries, alt))
                self.compute_options()

    def delete_option_by_index(self, index):
        if not self.exist_option_by_index(index):
            print("Index not found")
        self.entries.pop(Utils().get_index_from_list(self.entries, self.entries[index - 1]))
        self.compute_options()

    # TODO: multiple options
    def delete_option_by_key(self, key):
        alternatives = [key.upper(), key.lower()]
        for alt in alternatives:
            if Inspector().element_in_list(alt, self.options.keys()):
                print("Success")
                self.entries.pop(Utils().get_index_from_list(self.entries, self.options[alt]))
                self.compute_options()

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

    def one_option_already_exist(self, options):
        if not self.exist_one_option(list(options)):
            Utils().exception("One option already exist")
