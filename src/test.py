from src.components.Menu import Menu

menu = Menu("numbers", "test", "ajouter un client", "modifier un client", "supprimer un client")
menu.show()

menu.add_options("ajouter un produit", "ajouter un article")
menu.show()
