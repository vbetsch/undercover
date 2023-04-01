from app.src.components.Menu import Menu, MenuMode


class TestMenu:
    def __init__(self):
        self.menu = None

    # First letters

    def test1(self):
        self.menu = Menu(MenuMode.FIRST_LETTERS.value, "meNu", "Ajouter un client", "ModiFier un clieNt",
                         "supprimer un client")

    def test2(self):
        self.menu.add_options("Help")

    def test3(self):
        self.menu.add_options("JoUeR", "quItTer")

    def test4(self):
        self.menu.insert_options(s="rElier à Un cliEnT")

    def test5(self):
        self.menu.insert_options(h="XXxxxX", q="yYyyYY")

    def test6(self):
        self.menu.update_option("joUer", "Execute")

    def test7(self):
        self.menu.update_option_by_index(8, "pLay")

    def test8(self):
        self.menu.update_options_by_key(q="FerMer")

    def test9(self):
        self.menu.update_options_by_key(X="vOila", f="BREF")

    def test10(self):
        self.menu.delete_option("voilA")

    def test11(self):
        self.menu.delete_options_by_key('b')

    def test12(self):
        self.menu.delete_option_by_index(5)

    def test13(self):
        self.menu.add_options("JoUeR", "quItTer")

    def test14(self):
        self.menu.order(q=1, e=3)

    # Numbers

    def test15(self):
        self.menu = Menu(MenuMode.NUMBERS.value, "meNu", "Ajouter un client", "ModiFier un clieNt",
                         "supprimer un client")

    def test16(self):
        self.menu.add_options("Help")

    def test17(self):
        self.menu.add_options("JoUeR", "BREF")

    def test18(self):
        self.menu.add_options("rElier à Un cliEnT", "vOila", "yYyyYY")

    def test19(self):
        self.menu.update_option("joUer", "Execute")

    def test20(self):
        self.menu.update_option_by_index(8, "pLay")

    def test21(self):
        self.menu.delete_option("plAy")

    def test22(self):
        self.menu.delete_option('brEf')

    def test23(self):
        self.menu.delete_option_by_index(5)

    def test24(self):
        self.menu.add_options("JoUeR", "quItTer")

    # Main Menu

    def test25(self):
        self.menu = Menu("first_letters", "main", "resume", "create", "load", "delete", "quit")

    def test26(self):
        is_running = True
        while is_running:
            choice = input(f"{self.menu.text()}\n")
            match choice:
                case 'r':
                    print('Resume')
                case 'c':
                    print('Create')
                case 'l':
                    print('Load')
                case 'd':
                    print('Delete')
                case 'q':
                    is_running = False
                case _:
                    print("Option not found")
