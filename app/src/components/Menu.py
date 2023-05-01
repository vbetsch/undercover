from enum import Enum
from app.src.core.Inspector import Inspector
from app.src.core.Interactor import Interactor
from app.src.core.Utils import Utils


class MenuMode(Enum):
    FIRST_LETTERS = "first_letters"
    NUMBERS = "numbers"


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
        self.keys = []
        match self.mode:
            case MenuMode.FIRST_LETTERS.value:
                if Inspector().same_first_letter(self.entries):
                    Utils().exception(f"Some options start with same letter : <{self.entries}>")
                for entry in self.entries:
                    self.append_option(entry[0].lower(), entry.lower())
            case MenuMode.NUMBERS.value:
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

    def run(self):
        print(self.text())

    def bad_mode(self, mode):
        if self.mode == mode:
            Utils.exception(f"The mode menu <{mode}> could not use this method")

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

    @staticmethod
    def exist_option_by_index_of(entries, index):
        if index < 1 or index >= len(entries):
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

    def get_option_by_index(self, index):
        if not self.exist_option_by_index(index):
            Utils.exception(f"Index {index} not found")
        return self.options[index]

    def get_option_text_by_key(self, key):
        return self.get_option_by_key(key)['display']

    def get_index_from_key(self, key):
        return Utils().get_index_from_list(self.entries, self.get_option_text_by_key(key))

    def get_index_from_opt(self, opt):
        return Utils().get_index_from_list(self.entries, opt)

    def show(self, *indexes):
        for index in indexes:
            _index = index - 1
            if not self.exist_option_by_index(_index):
                Utils().exception(f"Index <{index}> not found")
            self.get_option_by_index(_index)['visible'] = True

    def show_by_keys(self, *keys):
        for key in keys:
            if not self.exist_option_by_index(self.get_index_from_key(key)):
                Utils().exception(f"Key <{key}> not found")
            self.get_option_by_key(key)['visible'] = True

    def hide(self, *indexes):
        for index in indexes:
            _index = index - 1
            if not self.exist_option_by_index(_index):
                Utils().exception(f"Index <{index}> not found")
            self.get_option_by_index(_index)['visible'] = False

    def hide_by_keys(self, *keys):
        for key in keys:
            if not self.exist_option_by_index(self.get_index_from_key(key)):
                Utils().exception(f"Key <{key}> not found")
            self.get_option_by_key(key)['visible'] = False

    def add_options(self, *entries):
        for entry in entries:
            self.entries.append(entry.lower())
        self.compute_options()

    def insert_options_by_key(self, **entries):
        self.bad_mode(MenuMode.NUMBERS.value)
        old_entries = self.entries.copy()
        for key, value in entries.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key <{key}> not found")
            self.entries.insert(old_entries.index(self.get_option_text_by_key(key)), value.lower())
        self.compute_options()

    def insert_options_by_index(self, *entries):
        for index, value in entries:
            if not self.exist_option_by_index(index):
                Utils().exception(f"Index <{index}> not found")
            self.entries.insert(index - 1, value)
        self.compute_options()

    def update_option(self, opt_display, entry):
        opt = opt_display.lower()
        if not self.exist_option(opt):
            Utils().exception(f"Option <{opt}> not found")
        self.entries[self.get_index_from_opt(opt)] = entry.lower()
        self.compute_options()

    def update_options_by_index(self, *indexes):
        for index, entry in indexes:
            _index = index - 1
            if not self.exist_option_by_index(_index):
                Utils().exception(f"Index <{index}> not found")
            self.entries[_index] = entry.lower()
            self.compute_options()

    def update_options_by_key(self, **keys):
        self.bad_mode(MenuMode.NUMBERS.value)
        for key, value in keys.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key <{key}> not found")
            self.update_option(self.get_option_text_by_key(key), value.lower())

    def order_by_key(self, **places):  # key -> index
        self.bad_mode(MenuMode.NUMBERS.value)
        # self.delete_options_by_key()
        for key in places.keys():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key <{key}> not found")
            if self.exist_key(key):
                self.entries.pop(self.get_index_from_key(key))
        # self.insert_options_by_key()
        for key, index in places.items():
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key <{key}> not found")
            self.entries.insert(index - 1, self.get_option_text_by_key(key).lower())
        self.compute_options()

    def order_by_index(self, *places):  # key -> index
        old_entries = self.entries.copy()
        for index, value in places:
            _index = index - 1
            _value = value - 1
            if not self.exist_option_by_index_of(old_entries, _index):
                Utils().exception(f"Index <{_index}> not found")
            self.entries.pop(_index)
            self.entries.insert(_value, self.get_option_text_by_key(index).lower())
        self.compute_options()

    def delete_option(self, opt_text):
        opt = opt_text.lower()
        if not self.exist_option(opt):
            Utils().exception(f"Option <{opt}> not found")
        if self.exist_option(opt):
            self.entries.pop(self.get_index_from_opt(opt))
            self.compute_options()

    def delete_option_by_index(self, index):
        _index = index - 1
        if not self.exist_option_by_index(_index):
            Utils().exception(f"Index <{index}> not found")
        self.entries.pop(Utils().get_index_from_list(self.entries, self.entries[_index]))
        self.compute_options()

    def delete_options_by_key(self, *keys):
        self.bad_mode(MenuMode.NUMBERS.value)
        for key in keys:
            key = key.lower()
            if not self.exist_key(key):
                Utils().exception(f"Key <{key}> not found")
            if self.exist_key(key):
                self.entries.pop(self.get_index_from_key(key))
                self.compute_options()
