### Mission : Créer une API de gestion de tâches (To-Do List) avec FastAPI et SQLite

**Objectif :** Créer une API pour gérer une liste de tâches (CRUD : Create, Read, Update, Delete) en utilisant FastAPI et stocker les données de manière persistante dans une base de données SQLite.

#### Détails de la Mission

1. **Préparer l'Environnement de Développement :**
   - Installer les bibliothèques nécessaires, y compris FastAPI, Uvicorn (pour exécuter l’API), et SQLAlchemy (pour gérer SQLite).

2. **Initialiser le Projet FastAPI :**
   - Créer un projet de base avec un fichier principal, comme `main.py`, pour définir l’application FastAPI et les routes.

3. **Configurer une Base de Données SQLite :**
   - Utiliser SQLAlchemy pour définir et gérer une base de données SQLite. Créer une configuration de base de données qui connecte l'application à un fichier de base de données local, par exemple `tasks.db`.

4. **Définir le Modèle de Données :**
   - Utiliser SQLAlchemy pour créer une classe de modèle qui représente une tâche dans la base de données, avec des champs comme **id**, **title**, **description**, et **completed** (pour indiquer si la tâche est terminée).
   - Configurer ce modèle pour créer la table correspondante dans la base de données lors de la première exécution.

5. **Créer les Routes de l’API :**
   - Définir les routes pour les quatre opérations CRUD :
     - **Créer** une nouvelle tâche : Ajouter une nouvelle tâche dans la base de données.
     - **Lire** toutes les tâches ou une tâche spécifique : Récupérer les tâches enregistrées dans la base de données.
     - **Mettre à jour** une tâche : Modifier les informations d’une tâche, comme le titre, la description, ou l’état d'achèvement.
     - **Supprimer** une tâche : Supprimer une tâche de la base de données.

6. **Tester l’API :**
   - Lancer le serveur FastAPI et tester chaque route via l'interface Swagger, disponible à l'adresse `/docs`.
   - Vérifier que chaque opération (ajout, modification, suppression, et lecture des tâches) fonctionne comme prévu et que les données sont bien enregistrées et récupérées de `tasks.db`.

7. **Ajouter des Fonctions Supplémentaires (Facultatif) :**
   - Ajouter des filtres pour afficher uniquement les tâches **complétées** ou **non complétées**.
   - Ajouter une route pour **marquer une tâche comme complétée** sans forcément modifier les autres champs.

Voici les commandes essentielles pour débuter avec FastAPI sous Windows, depuis l'initialisation de l'environnement jusqu'au démarrage du serveur.

### Étapes et Commandes à Connaître pour Débuter avec FastAPI et SQLite

1. **Initialiser un Environnement Virtuel :**
   - Il est recommandé de travailler dans un environnement virtuel pour éviter les conflits de dépendances entre projets.
   ```bash
   python -m venv env
   ```

2. **Activer l’Environnement Virtuel :**
   - Après avoir créé l’environnement, il faut l’activer.
   ```bash
   env\Scripts\activate
   ```

3. **Installer FastAPI et les Packages Nécessaires :**
   - Installer FastAPI pour construire l’API, Uvicorn pour lancer le serveur, et SQLAlchemy pour travailler avec SQLite.
   ```bash
   pip install fastapi uvicorn sqlalchemy
   ```

4. **Créer un Fichier `main.py` :**
   - Créer un fichier `main.py` dans lequel l’application et les routes seront définies. Pour le moment, il peut être vide ou contenir un simple message de bienvenue.

5. **Démarrer le Serveur avec Uvicorn en Mode Reload :**
   - Démarrer le serveur Uvicorn en mode **reload** pour que le serveur se redémarre automatiquement à chaque modification du code.
   ```bash
   uvicorn main:app --reload
   ```

   - Cette commande suppose que l'application FastAPI est définie dans un objet `app` dans le fichier `main.py`. Le serveur sera accessible à l’adresse `http://127.0.0.1:8000`.

6. **Tester l’API dans le Navigateur :**
   - Pour voir la documentation interactive, il suffit d’ouvrir un navigateur et de se rendre à l’adresse suivante :
   ```plaintext
   http://127.0.0.1:8000/docs
   ```

### Commandes Clés

| Commande                                    | Description                                                                                   |
|---------------------------------------------|-----------------------------------------------------------------------------------------------|
| `python -m venv venv`                        | Crée un environnement virtuel nommé `venv`.                                                   |
| `venv\Scripts\activate`                      | Active l’environnement virtuel sous Windows.                                                 |
| `pip install fastapi uvicorn sqlalchemy`    | Installe FastAPI, Uvicorn, et SQLAlchemy dans l’environnement virtuel.                       |
| `uvicorn main:app --reload`                 | Démarre le serveur Uvicorn en mode reload pour voir les modifications en direct.             |
| `http://127.0.0.1:8000/docs`                | Accès à l'interface Swagger pour tester et documenter l’API.                                 |

Ces commandes suffiront pour bien démarrer le projet FastAPI sur Windows et permettre des modifications dynamiques pendant le développement.