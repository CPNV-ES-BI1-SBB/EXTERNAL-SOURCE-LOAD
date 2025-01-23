# Étape 1 : Utiliser une image de base Python
FROM python:3.13.1-slim

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Installer les dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Etape 4 : Copier les fichiers de dépendances
COPY Pipfile Pipfile.lock /app/

# Étape 5 : Installer les dépendances Python
RUN pip install --no-cache-dir pipenv && \
    pipenv install --deploy

# Étape 6 : Copier les fichiers de l'application
COPY . /app

# Étape 7 : Exposer le port utilisé par FastAPI
EXPOSE 8000

# Étape 8 : Commande pour démarrer l'application
CMD ["pipenv", "run", "fastapi", "run"]
