from app.src.components.Menu import Menu


class TestMenu:
    def __init__(self):
        self.menu = None

    def test1(self):
        self.menu = Menu("first_letters", "tests", "ajouter un client", "modifier un client", "supprimer un client")

    def test2(self):
        self.menu.add_options("help")

    def test3(self):
        self.menu.add_options("jouer", "quitter")

    def test4(self):
        self.menu.insert_options(s="relier à un client")

    def test5(self):
        self.menu.insert_options(h="XXXXXX", q="YYYYYY")

    def test6(self):
        self.menu.update_option("jouer", "execute")

    def test7(self):
        self.menu.update_option_by_index(8, "play")

    def test8(self):
        self.menu.update_options_by_key(q="fermer")

    def test9(self):
        self.menu.update_options_by_key(X="voila", f="bref")

    def test10(self):
        self.menu.delete_option("voila")

    def test11(self):
        self.menu.delete_options_by_key('b')

    def test12(self):
        self.menu.delete_option_by_index(5)
