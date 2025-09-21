# lib/models/base.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Chemin absolu pour la base de données pour éviter les problèmes de chemin relatif
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(BASE_DIR, 'bibliotheque.db')

engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()