# lib/models/genre.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from .base import Base, session

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False, unique=True)

    # Relation : Un genre peut avoir plusieurs livres.
    books = relationship('Book', back_populates='genre')

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) < 3:
            raise ValueError("Le nom du genre doit être une chaîne de 3 caractères minimum.")
        self._name = value.strip()

    @classmethod
    def create(cls, name):
        """ Crée et enregistre un nouveau genre dans la BDD. """
        try:
            genre = cls(name=name)
            session.add(genre)
            session.commit()
            return genre
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la création du genre : {e}")
            return None

    @classmethod
    def get_all(cls):
        """ Retourne tous les genres de la BDD. """
        return session.query(cls).order_by(cls.id).all()

    @classmethod
    def find_by_id(cls, genre_id):
        """ Trouve un genre par son ID. """
        return session.query(cls).get(genre_id)

    def __repr__(self):
        return f"<Genre {self.id}: {self.name}>"