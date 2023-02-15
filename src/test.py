from src.components.Menu import Menu


def main():
    menu = Menu("first_letters", "test", "ajouter un client", "modifier un client", "supprimer un client")
    menu.show()
    
    menu.add_options("help")
    menu.show()
    
    menu.add_options("jouer", "quitter")
    menu.show()
    
    menu.insert_options((3, "relier à un client"))
    menu.show()
    
    menu.insert_options((5, "XXXXXX"), (6, "YYYYYY"))
    menu.show()
    
    menu.update_option("jouer", "execute")
    menu.show()
    
    menu.update_option_by_index(8, "play")
    menu.show()
    
    menu.update_option_by_key('q', "exit")
    menu.show()
    
    menu.delete_option("xxxxxx")
    menu.show()
    
    menu.delete_option_by_key("Y")
    menu.show()
    
    menu.delete_option_by_index(5)
    menu.show()


if __name__ == '__main__':
    main()
