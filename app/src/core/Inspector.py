from app.src.core.Meta import Singleton


class Inspector(metaclass=Singleton):
    def __init__(self):
        pass

    @staticmethod
    def element_in_list(element, array):
        if element in array:
            return True
        else:
            return False

    @staticmethod
    def same_first_letter(words):
        first_letters = []
        for word in words:
            first_letters.append(word.lower()[0])
        if len(first_letters) != len(set(first_letters)):
            return True
        else:
            return False

    @staticmethod
    def same_first_letter_without_case(words):
        first_letters = []
        for word in words:
            first_letters.append(word[0])
        if len(first_letters) != len(set(first_letters)):
            return True
        else:
            return False
