from src.components.Menu import Menu

menu = Menu("first_letters", "test", "ajouter un client", "modifier un client", "supprimer un client")
menu.show()

menu.add_options("jouer", "quitter")
menu.show()
