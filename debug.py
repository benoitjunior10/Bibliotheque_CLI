# debug.py
from lib.models.base import session
from lib.models.author import Author
from lib.models.book import Book
from lib.models.genre import Genre
import ipdb

# Exemples de code pour tester :
author1 = Author(name="J.K. Rowling")
genre1 = Genre(name = "Mystique")
book1 = Book(title="Harry Potter à l'école des sorciers", publication_year=1997, author=author1, genre=genre1)
session.add(author1)
session.add(book1)
session.add(genre1)
session.commit()

# Démarre une session de débogage interactive
ipdb.set_trace()