# lib/models/book.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from .base import Base, session
from .author import Author
from .genre import Genre

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    _title = Column("title", String, nullable=False)
    _publication_year = Column("publication_year", Integer)

    # Clé étrangère pour lier le livre a un auteur
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    # Clé étrangère pour lier le livre à un genre
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=True)
    
    # Relation : Un livre appartient a un seul auteur.
    author = relationship('Author', back_populates='books')
    # Relation : Un livre appartient à un seul genre.
    genre = relationship('Genre', back_populates='books')

    def __init__(self, title, publication_year, author, genre):
        self.title = title
        self.publication_year = publication_year
        self.author = author
        self.genre = genre

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Le titre ne peut pas être vide.")
        self._title = value.strip()
    
    @property
    def publication_year(self):
        return self._publication_year
    
    @publication_year.setter
    def publication_year(self, value):
        if not isinstance(value, int) or not (1000 <= value <= 2025): # Année de publication raisonnable
            raise ValueError("L'année de publication doit être un nombre valide.")
        self._publication_year = value

    @classmethod
    def create(cls, title, publication_year, author, genre):
        """ Crée et enregistre un nouveau livre dans la BDD. """
        try:
            book = cls(title=title, publication_year=publication_year, author=author, genre=genre)
            session.add(book)
            session.commit()
            return book
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la création du livre : {e}")
            return None

    def delete(self):
        """ Supprime le livre de la BDD. """
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        """ Retourne tous les livres de la BDD. """
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, book_id):
        """ Trouve un livre par son ID. """
        return session.query(cls).get(book_id)

    @classmethod
    def find_by_title(cls, title):
        """ Trouve un livre par son titre (insensible à la casse). """
        return session.query(cls).filter(cls._title.ilike(f"%{title}%")).first()

    def __repr__(self):
        return f"<Book {self.id}: {self.title} ({self.publication_year})>"