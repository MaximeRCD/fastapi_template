# FASTAPI Template
🚀 FastAPI Enterprise Template — Python 3.12+ Un template FastAPI haut de gamme pour entreprises, optimisé pour Python 3.12.  
Bien sûr ! Voici une **version adaptée explicitement pour Python 3.12**, avec des précisions sur la compatibilité, les avantages de cette version, et un README ajusté pour **mettre en avant l'utilisation de Python 3.12** dans un contexte professionnel.
J’intègre aussi quelques conseils spécifiques à Python 3.12, car certaines librairies ou outils sont désormais plus performants ou ont changé de syntaxe/compatibilité avec cette version.


---

### Présentation

Ce projet propose un socle FastAPI **moderne et robuste**, structuré pour exploiter toutes les dernières fonctionnalités et performances de **Python 3.12**. Parfait pour initier de nouveaux services web dans un contexte d’entreprise où qualité, rapidité de développement et maintenabilité sont essentiels.

---

### Points clés adaptés à Python 3.12

* **Exploite les nouveautés** : pattern matching, nouveaux types natifs, meilleures performances.
* **Packages et dépendances testés** pour Python 3.12 (FastAPI, SQLAlchemy, Pydantic v2+, etc.).
* **Compatibilité stricte** : gestion des dépendances et CI s’assurent que tout fonctionne sous Python 3.12.

---

### Fonctionnalités principales

* **Architecture professionnelle** et évolutive (prête pour la scalabilité, microservices, etc.)
* **Gestion des dépendances avec Poetry**, support Python 3.12+
* **Linting/formatage/typage** : Black, Ruff, isort, Flake8, mypy adaptés Python 3.12
* **Tests unitaires/integ.** : pytest, coverage
* **CI/CD GitHub Actions** (check Python 3.12, lint, test, doc, sécurité)
* **Pre-commit hooks** (formatage, lint, sécurité)
* **Documentation interactive et auto-générée** (Swagger, Redoc, mkdocs)
* **Logs structurés** (structlog/loguru)
* **Configuration moderne** (dotenv + Pydantic v2+)
* **Sécurité** (Bandit, check dépendances)
* **Utilitaire Makefile**

---

### Structure du projet

```shell
fastapi-enterprise-template/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
├── tests/
├── .github/
│   └── workflows/
├── .env.example
├── .pre-commit-config.yaml
├── pyproject.toml
├── Makefile
├── README.md
├── mkdocs.yml
└── LICENSE
```

---

### Dépendances et outils (compatibles Python 3.12)

* **Poetry** (`pyproject.toml` défini `python = "^3.12"`)
* **FastAPI**, **Uvicorn**
* **Pydantic v2+** (nécessaire pour support Python 3.12)
* **SQLAlchemy 2.0+**
* **Black**, **isort**, **Ruff** (100% compatibles et rapides sur 3.12)
* **pytest**, **pytest-cov**
* **mypy** (dernière version pour support 3.12)
* **Bandit**
* **pre-commit**
* **mkdocs**

---

### Installation et démarrage

```bash
# Clonage et setup Python 3.12+
git clone https://github.com/ton-orga/fastapi-enterprise-template.git
cd fastapi-enterprise-template

# Installation avec Poetry (qui vérifie la version Python)
poetry install

# Copier le fichier d'exemple d'environnement
cp .env.example .env

# Lancer l’API (développement)
make run

# API docs sur http://localhost:8000/docs
```

---

### Pre-commit, lint, tests

```bash
# Installer les hooks pre-commit (obligatoire dès le 1er commit)
poetry run pre-commit install

# Lancer les lint/format/check
make lint
make format
make typecheck

# Lancer les tests
make test
```

---

### CI/CD

* **GitHub Actions** : pipeline pour Python 3.12, check lint, tests, couverture, sécurité, doc.
* **Badge de build** dans le README.
* **Facilement adaptable à d’autres outils CI.**

---

### Documentation

* **API** : Swagger (OpenAPI) et Redoc intégrés à FastAPI.
* **Projet** : mkdocs (toute la doc développeur en markdown, facilement hébergeable).
* **Type hints** partout (profitez des améliorations typing 3.12 !).

---

### Avantages Python 3.12

* **Meilleures performances** (CPython optimisé)
* **Nouveaux types** (`Self`, `typing.Any`, etc)
* **Pattern matching** avancé
* **Nouvelles APIs** dans standard lib, syntaxe plus moderne
* **Support long terme et sécurité**

---

### Conseils d’utilisation en entreprise

* **Utilisez toujours un virtualenv Python 3.12 local au projet.**
* **Gardez vos dépendances à jour (voir `make upgrade-deps`).**
* **Vérifiez la compatibilité des nouvelles libs avec Python 3.12.**
* **Code review systématique, coverage > 90%.**
* **Docs et tests à chaque feature.**
* **Déploiement sur des environnements Python 3.12 (Docker base image recommandée : `python:3.12-slim`).**

---

## Extrait du pyproject.toml (important !)

```toml
[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.111"
uvicorn = "^0.30"
pydantic = "^2.7"
sqlalchemy = "^2.0"
...

[tool.poetry.group.dev.dependencies]
black = "^24.4"
isort = "^5.13"
ruff = "^0.4"
pytest = "^8.2"
pytest-cov = "^5.0"
mypy = "^1.10"
bandit = "^1.7"
pre-commit = "^3.7"
mkdocs = "^1.6"
```

---

## 🔖 Recommandations avancées

### 📋 Modèles d’issues et de Pull Requests (GitHub)

* **Pourquoi ?** Standardiser les échanges, garantir des informations claires pour le suivi et la review.
* **Comment ?**

  * Ajoutez des fichiers dans `.github/ISSUE_TEMPLATE/` pour différents types de tickets : bug, amélioration, documentation, question…
  * Créez `.github/pull_request_template.md` pour guider les contributeurs (description de la PR, checklist tests/lint, impacts breaking, etc).
  * Exemple :

    ```md
    # pull_request_template.md

    ## Objectif de la PR

    ## Résumé des modifications

    ## Checklist
    - [ ] Code linté/formaté
    - [ ] Tests passants/localement
    - [ ] Couverture maintenue
    - [ ] Documentation mise à jour
    - [ ] Pas de breaking change involontaire

    ## Screenshots/Logs éventuels
    ```
  * Voir [GitHub Docs - Issue and PR templates](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issue-templates-for-your-repository).

---

### 🐳 Fichiers Docker (python:3.12-slim)

* **Pourquoi ?** Garantir l’exécution identique partout, CI, staging, prod.
* **Bonnes pratiques :**

  * Base image : `python:3.12-slim`
  * Utilisation de **Poetry** pour la gestion des dépendances
  * Réduction de la taille d’image (install dépendances système minimales, clean cache pip/apt)
  * `.dockerignore` propre (exclure tests, venv, cache, etc.)
* **Exemple Dockerfile minimal :**

  ```Dockerfile
  FROM python:3.12-slim

  # Installation des dépendances système minimales
  RUN apt-get update && apt-get install -y gcc libpq-dev

  # Configuration locale
  ENV POETRY_VERSION=1.8.3
  RUN pip install "poetry==$POETRY_VERSION"

  # Copie du projet et des fichiers Poetry
  WORKDIR /app
  COPY pyproject.toml poetry.lock* ./
  RUN poetry install --only main

  # Copie du code source
  COPY app ./app

  # Lancement de l’API
  CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

  * Pour le dev, ajoutez un `docker-compose.yml` avec un service pour la base de données !

---

### 🗄 Scripts de migration DB (SQLAlchemy 2.0+ & Alembic)

* **Pourquoi ?** Gérer l’évolution du schéma de BDD sans douleur, versionner les changements, permettre rollback.
* **Recommandations :**

  * Utilisez **Alembic** (compatible SQLAlchemy 2.0+) pour la gestion des migrations :

    * Génération auto via modèles (autogenerate) mais toujours relire le diff !
    * Versionnez le dossier `migrations/` dans le repo.
    * Ajoutez un raccourci dans le `Makefile` pour les commandes courantes (migration, upgrade, downgrade).
    * Gardez vos modèles synchronisés avec la BDD (doctrine “models as single source of truth”).
    * Exécutez les migrations automatiquement au démarrage (pour les environnements dev/staging).
  * Exemple Makefile :

    ```make
    migrate:
    	poetry run alembic revision --autogenerate -m "Migration"
    upgrade:
    	poetry run alembic upgrade head
    downgrade:
    	poetry run alembic downgrade -1
    ```
* **Doc utile :**
  [Alembic for SQLAlchemy 2.0](https://alembic.sqlalchemy.org/en/latest/changelog.html#version-1-10-0)

---

### ⚡️ Exemples de services async/await optimisés (FastAPI & Python 3.12)

* **Pourquoi ?** Profiter pleinement de l’asynchronicité, améliorer la scalabilité et la rapidité des traitements IO-bound (appels DB, APIs externes, fichiers…).
* **Recommandations :**

  * **Utilisez async/await partout où possible** (routes, services, requêtes DB avec async SQLAlchemy, HTTPX pour les appels externes, etc).
  * Privilégiez les clients asynchrones :

    * DB : [SQLAlchemy AsyncIO](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
    * HTTP : [httpx.AsyncClient](https://www.python-httpx.org/async/)
  * Structurez vos services pour la réutilisabilité et les tests (injection de dépendance via FastAPI).
* **Exemple de service async** :

  ```python
  # app/services/user_service.py

  from app.db.session import async_session
  from app.models import User
  from sqlalchemy.future import select

  async def get_user_by_email(email: str) -> User | None:
      async with async_session() as session:
          result = await session.execute(select(User).where(User.email == email))
          return result.scalar_one_or_none()
  ```
* **Tests** : Utilisez `pytest-asyncio` pour tester les fonctions asynchrones.
* **Docs utiles** :
  [FastAPI - Async SQL Databases](https://fastapi.tiangolo.com/advanced/async-sql-databases/)

Avec plaisir !
Tu trouveras ci-dessous :

* **Modèles de fichiers** pour GitHub (issues, pull request)
* **Dockerfile** complet pour Python 3.12 avec Poetry
* **docker-compose.yml** pour dev (FastAPI + Postgres)
* **Exemple .dockerignore**
* **Config Alembic** et **Makefile** pour migrations
* **Exemple de service async/await**

- Bonus : fichier pyproject.toml minimal pour tout lier.

---

## 1. Modèles GitHub

### `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
name: 🐛 Bug Report
description: Signaler un bug pour qu’on puisse le corriger rapidement !
labels: [bug]
body:
  - type: markdown
    attributes:
      value: |
        Merci de remplir les informations suivantes avec le plus de détails possible.
  - type: input
    id: environment
    attributes:
      label: Environnement
      description: (ex : OS, version Python, Docker, ...)
  - type: textarea
    id: description
    attributes:
      label: Description du bug
      description: Que s’est-il passé ? Quelle est la conséquence ?
  - type: textarea
    id: steps
    attributes:
      label: Étapes pour reproduire
      description: Liste détaillée
  - type: textarea
    id: logs
    attributes:
      label: Logs/erreurs
      description: Copiez les messages d’erreur (si applicables)
```

### `.github/pull_request_template.md`

```markdown
## Objectif de la PR

<!-- Expliquer en 1-2 phrases ce que fait cette PR -->

## Résumé des modifications principales

-

## Checklist
- [ ] Lint/Format ok (`make lint`)
- [ ] Tests passent (`make test`)
- [ ] Documentation mise à jour
- [ ] Breaking change ? (oui/non, détaillez si oui)
- [ ] PR liée à une issue ? (référence)

## Screenshots / Logs éventuels

```

---

## 2. Docker

### `Dockerfile`

```dockerfile
FROM python:3.12-slim

# Dépendances système (ajuster si besoin, ex. pour Postgres, C, ...)
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Installer Poetry
ENV POETRY_VERSION=1.8.3
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --only main

# Copier le code
COPY app ./app

# Copier fichiers Alembic pour les migrations DB si besoin
COPY alembic.ini .
COPY migrations ./migrations

# Pour Uvicorn / FastAPI
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### `.dockerignore`

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
.env
.venv
tests/
.git
.gitignore
docker-compose.yml
alembic.ini
migrations/
*.db
```

---

### `docker-compose.yml`

```yaml
version: '3.8'
services:
  api:
    build: .
    env_file:
      - .env
    ports:
      - "8000:8000"
    depends_on:
      - db
    volumes:
      - ./app:/app/app  # Live reload en dev
      - ./migrations:/app/migrations
      - ./alembic.ini:/app/alembic.ini

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

---

## 3. Alembic (SQLAlchemy 2.0+)

### `alembic.ini` (extrait minimal)

```ini
[alembic]
script_location = migrations
sqlalchemy.url = postgresql+psycopg2://user:password@db:5432/mydb
```

### `migrations/env.py` (adapté async SQLAlchemy)

```python
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.db.models import Base  # Ajuster selon arborescence

# Config Alembic
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(url=config.get_main_option("sqlalchemy.url"), target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.', poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

---

### `Makefile`

```makefile
run:
	poetry run uvicorn app.main:app --reload

lint:
	poetry run ruff check app
	poetry run black --check app

format:
	poetry run black app
	poetry run isort app

test:
	poetry run pytest tests

migrate:
	poetry run alembic revision --autogenerate -m "Migration"

upgrade:
	poetry run alembic upgrade head

downgrade:
	poetry run alembic downgrade -1
```

---

## 4. Service Python async/await

### `app/services/user_service.py`

```python
from app.db.session import async_session
from app.models.user import User
from sqlalchemy import select

async def get_user_by_email(email: str) -> User | None:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
```

> ⚡️ Penser à importer et utiliser ce service avec des routes FastAPI `async def`.

---

### Exemple de test async (pytest-asyncio)

```python
import pytest
from app.services.user_service import get_user_by_email

@pytest.mark.asyncio
async def test_get_user_by_email():
    user = await get_user_by_email("test@example.com")
    assert user is None or user.email == "test@example.com"
```

---

## 5. Extrait `pyproject.toml` (Python 3.12 & tous outils)

```toml
[tool.poetry]
name = "fastapi-enterprise-template"
version = "0.1.0"
description = "FastAPI starter template entreprise Python 3.12"
authors = ["Ton Nom <email@tonmail.com>"]
readme = "README.md"
packages = [{include = "app"}]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.111"
uvicorn = "^0.30"
pydantic = "^2.7"
sqlalchemy = "^2.0"
asyncpg = "^0.29"

[tool.poetry.group.dev.dependencies]
black = "^24.4"
isort = "^5.13"
ruff = "^0.4"
pytest = "^8.2"
pytest-cov = "^5.0"
pytest-asyncio = "^0.23"
mypy = "^1.10"
bandit = "^1.7"
pre-commit = "^3.7"
mkdocs = "^1.6"
alembic = "^1.13"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```




