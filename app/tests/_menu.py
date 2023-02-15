from app.src.components.Menu import Menu


class TestMenu:
    def __init__(self):
        self.menu = None

    def test1(self):
        self.menu = Menu("first_letters", "tesTs", "Ajouter un client", "ModiFier un clieNt", "supprimer un client")

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
