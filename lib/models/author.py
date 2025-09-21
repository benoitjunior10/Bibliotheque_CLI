# lib/models/author.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from .base import Base, session

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False, unique=True)

    # Relation : Un auteur a plusieurs livres.
    # Si un auteur est supprimé, ses livres le sont aussi (cascade).
    books = relationship('Book', back_populates='author', cascade='all, delete-orphan')

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Le nom doit être une chaîne de 2 caractères minimum.")
        self._name = value.strip()

    @classmethod
    def create(cls, name):
        """ Crée et enregistre un nouvel auteur dans la BDD. """
        try:
            author = cls(name=name)
            session.add(author)
            session.commit()
            return author
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la création de l'auteur : {e}")
            return None

    def delete(self):
        """ Supprime l'auteur de la BDD. """
        session.delete(self)
        session.commit()

    @classmethod
    def get_all(cls):
        """ Retourne tous les auteurs de la BDD. """
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, author_id):
        """ Trouve un auteur par son ID. """
        return session.query(cls).get(author_id)
    
    @classmethod
    def find_by_name(cls, name):
        """ Trouve un auteur par son nom (insensible à la casse). """
        return session.query(cls).filter(cls._name.ilike(f"%{name}%")).first()

    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"