# lib/cli.py
from .helpers import (
    exit_program,
    list_all_authors,
    add_new_author,
    find_author_menu,
    list_all_books,
    add_new_book,
    delete_book_menu,
    list_all_genres,
    add_new_genre,
    find_genre_menu,
)

def main_menu():
    while True:
        # m use yon dict pou chwa user yo
        menu_options = {
            "1": ("Gérer les Auteurs", author_menu),
            "2": ("Gérer les Livres", book_menu),
            "3": ("Gérer les Genres", genre_menu),
            "0": ("Quitter l'application", exit_program),
        }
        print("\n=== Menu Principal de la Bibliothèque ===")
        for key, (text, _) in menu_options.items():
            print(f"  {key}. {text}")
        
        choice = input("Votre choix : ")
        action = menu_options.get(choice)

        if action:
            action[1]() # Exécute la fonction associée
        else:
            print("❌ Choix invalide, veuillez reessayer.")

def author_menu():
    while True:
        print("\n--- Menu Auteurs ---")
        print("  1. Voir tous les auteurs")
        print("  2. Ajouter un nouvel auteur")
        print("  3. Rechercher un auteur")
        print("  0. Retourner au menu principal")
        choice = input("Votre choix : ")

        if choice == '1':
            list_all_authors()
        elif choice == '2':
            add_new_author()
        elif choice == '3':
            find_author_menu()
        elif choice == '0':
            break
        else:
            print("❌ Choix invalide, veuillez reessayer.")

def book_menu():
    while True:
        print("\n--- Menu Livres ---")
        print("  1. Voir tous les livres")
        print("  2. Ajouter un nouveau livre")
        print("  3. Supprimer un livre")
        print("  0. Retourner au menu principal")
        choice = input("Votre choix : ")

        if choice == '1':
            list_all_books()
        elif choice == '2':
            add_new_book()
        elif choice == '3':
            delete_book_menu()
        elif choice == '0':
            break
        else:
            print("❌ Choix invalide, veuillez reessayer.")
            
def genre_menu():
    while True:
        print("\n--- Menu Genres ---")
        print("  1. Voir tous les genres")
        print("  2. Ajouter un nouveau genre")
        print("  3. Voir les livres par genre")
        print("  0. Retourner au menu principal")
        choice = input("Votre choix : ")

        if choice == '1':
            list_all_genres()
        elif choice == '2':
            add_new_genre()
        elif choice == '3':
            find_genre_menu()
        elif choice == '0':
            break
        else:
            print("❌ Choix invalide, veuillez reessayer.")

def start():
    """Point d'entrée pour démarrer la CLI."""
    print("📚 Bienvenue dans le gestionnaire de bibliothèque ! 📚")
    main_menu()