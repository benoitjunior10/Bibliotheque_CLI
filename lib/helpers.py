# lib/helpers.py
from .models.author import Author
from .models.book import Book
from .models.genre import Genre

def exit_program():
    print("Au revoir !")
    exit()

# --- Fonctions pour les Auteurs ---

def list_all_authors():
    authors = Author.get_all()
    if not authors:
        print("Aucun auteur trouvé dans la bibliothèque.")
    else:
        print("--- Liste des Auteurs ---")
        for author in authors:
            print(f"  ID: {author.id} | Nom: {author.name}")
    print("-" * 25)

def add_new_author():
    while True:
        name = input("Entrez le nom complet de l'auteur : ")
        try:
            author = Author.create(name)
            if author:
                print(f"✅ L'auteur '{author.name}' a été ajouté avec succès !")
            break
        except ValueError as e:
            print(f"❌ Erreur de validation : {e}. Veuillez réessayer.")

def find_author_menu():
    name = input("Entrez le nom de l'auteur à rechercher : ")
    author = Author.find_by_name(name)
    if author:
        display_author_details(author)
    else:
        print(f"❌ Aucun auteur correspondant à '{name}' n'a été trouvé.")

def display_author_details(author):
    print("\n--- Détails de l'Auteur ---")
    print(f"  Nom : {author.name}")
    print("  Livres publiés :")
    if author.books:
        # Utilisation d'une liste de tuples pour stocker les infos avant l'affichage
        book_info = [(book.title, book.publication_year, book.genre.name if book.genre else "N/A") for book in author.books]
        for title, year, genre_name in book_info:
            print(f"    - {title} ({year}) - Genre: {genre_name}")
    else:
        print("    Cet auteur n'a aucun livre enregistré.")
    print("-" * 27)

# --- Fonctions pour les Genres ---

def list_all_genres():
    genres = Genre.get_all()
    if not genres:
        print("Aucun genre trouvé.")
    else:
        print("\n--- Genres Disponibles ---")
        for genre in genres:
            print(f"  ID: {genre.id} | Nom: {genre.name}")
    print("-" * 26)
    return genres

def add_new_genre():
    while True:
        name = input("Entrez le nom du nouveau genre : ")
        try:
            genre = Genre.create(name)
            if genre:
                print(f"✅ Le genre '{genre.name}' a été créé avec succès !")
            return genre
        except ValueError as e:
            print(f"❌ {e}. Veuillez réessayer.")

def find_genre_menu():
    list_all_genres()
    try:
        genre_id = int(input("Entrez l'ID du genre pour voir ses livres : "))
        genre = Genre.find_by_id(genre_id)
        if genre:
            print(f"\n--- Livres du genre '{genre.name}' ---")
            if genre.books:
                for book in genre.books:
                    print(f"  - '{book.title}' par {book.author.name}")
            else:
                print("  Aucun livre trouvé pour ce genre.")
            print("-" * 30)
        else:
            print("❌ Genre non trouvé.")
    except ValueError:
        print("❌ ID invalide.")

# --- Fonctions pour les Livres ---

def add_new_book():
    print("\n--- Ajout d'un nouveau livre ---")
    title = input("Titre du livre : ")
    if not title:
        print("❌ Le titre ne peut pas être vide. Annulation.")
        return

    try:
        year = int(input("Année de publication : "))
    except ValueError:
        print("❌ Année invalide. Annulation.")
        return

    author_name = input("Nom de l'auteur : ")
    author = Author.find_by_name(author_name)

    if not author:
        print(f"L'auteur '{author_name}' n'existe pas.")
        if input("Voulez-vous le créer ? (o/n) : ").lower() == 'o':
            try:
                author = Author.create(author_name)
                if not author: return
                print(f"✅ Auteur '{author.name}' créé.")
            except ValueError as e:
                print(f"❌ {e}. Annulation.")
                return
        else:
            return

    genre = select_or_create_genre()
    if not genre:
        print("❌ Aucun genre sélectionné. Création du livre annulée.")
        return

    try:
        book = Book.create(title, year, author, genre)
        if book:
            print(f"✅ Le livre '{book.title}' par {author.name} a été ajouté avec succès !")
    except ValueError as e:
        print(f"❌ Erreur de validation : {e}. Annulation.")

def select_or_create_genre():
    """Aide l'utilisateur à choisir un genre existant ou à en créer un nouveau."""
    while True:
        genres = list_all_genres()
        choice = input("Entrez l'ID du genre ou tapez 'nouveau' pour en créer un : ").lower()
        if choice == 'nouveau':
            return add_new_genre()
        try:
            genre_id = int(choice)
            genre = next((g for g in genres if g.id == genre_id), None)
            if genre:
                return genre
            else:
                print("❌ ID invalide. Veuillez réessayer.")
        except ValueError:
            print("❌ Entrée invalide. Veuillez entrer un ID ou 'nouveau'.")

def list_all_books():
    books = Book.get_all()
    if not books:
        print("Aucun livre trouvé dans la bibliothèque.")
    else:
        print("--- Liste de tous les Livres ---")
        for book in books:
            author_name = book.author.name if book.author else "Inconnu"
            genre_name = book.genre.name if book.genre else "N/A"
            print(f"  '{book.title}' par {author_name} ({book.publication_year}) - Genre: {genre_name}")
    print("-" * 33)

def delete_book_menu():
    title = input("Entrez le titre du livre à supprimer : ")
    book = Book.find_by_title(title)
    if book:
        if input(f"Êtes-vous sûr de vouloir supprimer '{book.title}' par {book.author.name} ? (o/n) : ").lower() == 'o':
            book.delete()
            print(f"✅ Le livre '{book.title}' a été supprimé.")
        else:
            print("Suppression annulée.")
    else:
        print(f"❌ Aucun livre correspondant à '{title}' n'a été trouvé.")