# Gestionnaire de Bibliothèque CLI

## Description

Cette application est une interface en ligne de commande (CLI) en Python pour gérer une petite bibliothèque. Elle permet aux utilisateurs de gérer des auteurs, des livres et les genres, en utilisant SQLAlchemy comme ORM pour interagir avec une base de données SQLite.

Le projet met l'accent sur une expérience utilisateur simple et contextuelle, en séparant clairement la logique de l'interface, la logique métier et l'accès aux données.

## Fonctionnalités

- **Gestion des Auteurs**
  - Lister tous les auteurs.
  - Ajouter un nouvel auteur avec validation du nom.
  - Rechercher un auteur par son nom.
  - Afficher les détails d'un auteur, y compris la liste de ses livres et leur genre.
  - Supprimer un auteur (ce qui supprime également tous les livres associés).

- **Gestion des Livres**
  - Lister tous les livres avec leur auteur et leur genre.
  - Ajouter un nouveau livre en l'associant à un auteur et à un genre (existants ou nouveaux).
  - Supprimer un livre par son titre.

- **Gestion des Genres**
  - Lister tous les genres.
  - Ajouter un nouveau genre.
  - Afficher tous les livres appartenant à un genre spécifique.

## Installation et Lancement

1.  **Clonez le dépôt :**
    ```bash
    git clone <URL_DU_DEPOT>
    cd bibliotheque_cli
    ```

2.  **Installez les dépendances avec Pipenv :**
    Assurez-vous d'avoir `pipenv` installé (`pip install pipenv`).
    ```bash
    pipenv install
    ```

3.  **Activez l'environnement virtuel :**
    ```bash
    pipenv shell
    ```

4.  **Lancez l'application :**
    ```bash
    python main.py
    ```
    La première exécution créera automatiquement le fichier de base de données `bibliotheque.db`.

## Structure du Projet

```
bibliotheque_cli/
├── lib/
│   ├── models/       # Modèles ORM (Author, Book, Genre)
│   ├── cli.py        # Logique de l'interface utilisateur
│   └── helpers.py    # Fonctions de logique métier
├── main.py           # Point d'entrée de l'application
├── Pipfile           # Dépendances
└── README.md
```

## Modèles de Données

-   **Author** :
    -   `id`: `Integer` (clé primaire)
    -   `name`: `String` (nom de l'auteur)

-   **Genre** :
    -   `id`: `Integer` (clé primaire)
    -   `name`: `String` (nom du genre)

-   **Book** :
    -   `id`: `Integer` (clé primaire)
    -   `title`: `String` (titre du livre)
    -   `publication_year`: `Integer` (année de publication)
    -   `author_id`: `Integer` (clé étrangère liant a `Author`)
    -   `genre_id` : `Integer` (clé étrangère liant a `Genre`)

Il existe une relation **un-à-plusieurs** entre `Author` et `Book`, ainsi qu'entre `Genre` et `Book`.