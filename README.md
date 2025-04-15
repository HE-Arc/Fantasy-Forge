![Logo](https://github.com/user-attachments/assets/492ddb69-e607-42ab-9930-7be3705c18fc)

## Description

Projet créé dans le cadre de la HE-Arc pendant le semestre de printemps pour le cours 3259.2 Développement web II.
Le but est de créer une application web de gestion de parties DnD utilisant le framework Django pour le backend et Vue.js pour le frontend.

## Dépendances
- Node.js >= 18.0
- Python >= 3.12

## Installer le projet en local
1. Cloner le répertoire git
2. Créer un fichier .env et le configurer comme il se doit. Plusieurs fichiers .env seront nécessaires, un à la racine du dossier `api` pour la base de données postgres (à créer en local si c'est pas déjà fait), l'autre à la racine de `frontend`.
Voici un exemple de configuration:
    - `api`
      
      ```
      DB_NAME=fantasy_forge
      DB_USER=fantasy_forge
      DB_PASSWORD=# à choix
      DB_HOST=localhost
      DB_PORT=5432
      ```
      
    - `frontend`
    
      ```
      VITE_API_URL=http://localhost:8000/
      VITE_DND_API_URL=https://www.dnd5eapi.co/api/2014/
      ```
3. Générer un environnement virtuel avec pipenv dans `api`
   
     ```
     pip install pipenv # si nécessaire
     pipenv install
     ```
5. Entrer dans l'environnement et faire tourner la partie backend du serveur en mode dev
     ```
     pipenv shell
     python manage.py migrate # migration pour peupler la bd la première fois
     python manage.py runserver
     ```
6. Vérifier si Django marche en allant à l'URL suivant: http://localhost:8000/
7. Aller dans `frontend`, installer les dépendances Vue.js, puis faire tourner la partie frontend en mode dev
    ```
    npm install
    npm run dev
    ```
8. Vérifier si Vue.js marche en allant à l'URL suivant: http://localhost:5173/
     
