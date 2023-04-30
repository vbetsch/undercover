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
        self.menu.insert_options_by_key(s="rElier à Un cliEnT")

    def test5(self):
        self.menu.insert_options_by_key(h="XXxxxX", q="yYyyYY")

    def test6(self):
        self.menu.update_option("joUer", "Execute")

    def test7(self):
        self.menu.update_options_by_index((8, "pLay"))

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
        self.menu.order_by_key(j=1, q=6)

    # Numbers

    def test15(self):
        self.menu = Menu(MenuMode.NUMBERS.value, "meNu", "Ajouter un client", "ModiFier un clieNt",
                         "supprimer un client")

    def test16(self):
        self.menu.add_options("Help")

    def test17(self):
        self.menu.add_options("JoUeR", "quItTer")

    def test18(self):
        self.menu.insert_options_by_index((3, "rElier à Un cliEnT"))

    def test19(self):
        self.menu.insert_options_by_index((5, "XXxxxX"), (7, "yYyyYY"))

    def test20(self):
        self.menu.update_option("joUer", "Execute")

    def test21(self):
        self.menu.update_options_by_index((8, "pLay"))

    def test22(self):
        self.menu.update_options_by_index((9, "FerMer"))

    def test23(self):
        self.menu.update_options_by_index((5, "vOila"), (9, "BREF"))

    def test24(self):
        self.menu.delete_option("voilA")

    def test25(self):
        self.menu.delete_option_by_index(8)

    def test26(self):
        self.menu.delete_option_by_index(5)

    def test27(self):
        self.menu.add_options("JoUeR", "quItTer")

    # def test28(self):
    #     self.menu.order_by_index((7, 1), (8, 6))

    # Main Menu

    # def test25(self):
    #     self.menu = Menu("first_letters", "main", "resume", "create", "load", "delete", "quit")

    # def test26(self):
    #     is_running = True
    #     while is_running:
    #         choice = input(f"{self.menu.text()}\n")
    #         match choice:
    #             case 'r':
    #                 print('Resume')
    #             case 'c':
    #                 print('Create')
    #             case 'l':
    #                 print('Load')
    #             case 'd':
    #                 print('Delete')
    #             case 'q':
    #                 is_running = False
    #             case _:
    #                 print("Option not found")
