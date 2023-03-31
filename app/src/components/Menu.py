from app.src.core.Inspector import Inspector
from app.src.core.Interactor import Interactor
from app.src.core.Utils import Utils


class Menu:
    def __init__(self, mode, title, *entries):
        self.mode = mode
        self.title = title
        self.options = []
        self.entries = []
        self.keys = []
        for entry in entries:
            self.entries.append(entry.lower())
        self.compute_options()

    def append_option(self, key, value):
        self.keys.append(key)
        new_option = {
            "key": key,
            "display": value,
            "visible": True
        }
        self.options.append(new_option)

    def compute_options(self):
        self.options = []
        match self.mode:
            case "first_letters":
                if Inspector().same_first_letter(self.entries):
                    Utils().exception("Some options start with same letter")
                for entry in self.entries:
                    self.append_option(entry[0].lower(), entry.lower())
            case "numbers":
                for index in range(0, len(self.entries)):
                    self.append_option(index + 1, self.entries[index].lower())
            case _:
                Utils().exception(Interactor().trad("menu", "_menu_mode_not_found"))

    def text(self):
        result = f"--------------- {self.title.upper()} ---------------"
        for opt in self.options:
            if opt["visible"]:
                result += f"\n({opt['key']}) {opt['display'].capitalize()}"
        return result

    def show(self):
        print(self.text())

    def exist_key(self, key):
        if Inspector().element_in_list(key.lower(), self.keys):
            return True
        else:
            return False

    def exist_option(self, opt_display):
        if Inspector().element_in_list(opt_display.lower(), self.entries):
            return True
        else:
            return False

    def exist_option_by_index(self, index):
        if index < 1 or index >= len(self.entries):
            return False
        else:
            return True

    def exist_one_option(self, options_display):
        for opt in options_display:
            if self.exist_option(opt):
                return True
        return False

    def exist_all_options(self, options_display):
        for opt in options_display:
            if not self.exist_option(opt):
                return False
        return True

    def get_option_by_key(self, key):
        if key not in self.keys:
            Utils.exception(f"Key {key} not found")
        for opt in self.options:
            if opt['key'] == key:
                return opt

    def get_option_text_by_key(self, key):
        return self.get_option_by_key(key)['display']

    def get_index_from_key(self, key):
        return Utils().get_index_from_list(self.entries, self.get_option_text_by_key(key))

    def get_index_from_opt(self, opt):
        return Utils().get_index_from_list(self.entries, opt)

    def add_options(self, *entries):
        for entry in entries:
            self.entries.append(entry.lower())
        self.compute_options()

    def insert_options(self, **entries):
        if self.mode == "numbers":
            # Utils.exception(f"The mode menu {self.mode} could not use the method 'insert_options'")
            return "The actual mode menu could not use the method 'insert_options'"
        for key, value in entries.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            self.entries.insert(self.entries.index(self.get_option_text_by_key(key)), value.lower())
        self.compute_options()

    def update_option(self, opt_display, entry):
        opt = opt_display.lower()
        if not self.exist_option(opt):
            Utils().exception(f"Option {opt} not found")
        self.entries[self.get_index_from_opt(opt)] = entry.lower()
        self.compute_options()

    def update_option_by_index(self, index, entry):
        if not self.exist_option_by_index(index):
            Utils().exception(f"Index {index} not found")
        self.entries[index - 1] = entry.lower()
        self.compute_options()

    def update_options_by_key(self, **keys):
        for key, value in keys.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            self.update_option(self.get_option_text_by_key(key), value.lower())

    def order(self, **places):  # key -> index
        # self.delete_options_by_key()
        for key in places.keys():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            if self.exist_key(key):
                self.entries.pop(self.get_index_from_key(key))
        # self.insert_options()
        for key, index in places.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            self.entries.insert(index - 1, self.get_option_text_by_key(key).lower())
        self.compute_options()

    def delete_option(self, opt_text):
        opt = opt_text.lower()
        if not self.exist_option(opt):
            Utils().exception("Option not found")
        if self.exist_option(opt):
            self.entries.pop(self.get_index_from_opt(opt))
            self.compute_options()

    def delete_option_by_index(self, index):
        if not self.exist_option_by_index(index):
            Utils().exception("Index not found")
        self.entries.pop(Utils().get_index_from_list(self.entries, self.entries[index - 1]))
        self.compute_options()

    def delete_options_by_key(self, *keys):
        for key in keys:
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key {key} not found")
            if self.exist_key(key):
                self.entries.pop(self.get_index_from_key(key))
                self.compute_options()
