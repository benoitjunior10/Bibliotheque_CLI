# main.py
from lib.models.base import Base, engine
from lib.cli import start

if __name__ == "__main__":
    # Cree les tables dans la base de donnees si elles n'existent pas.
    Base.metadata.create_all(engine)
    
    # Lance l'application.
    start()