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

## À venir :

* Modèles d’issue/PR GitHub
* Fichiers de configuration Docker (python:3.12-slim, etc.)
* Scripts de migration DB adaptés SQLAlchemy 2.0+
* Exemples de services async/await optimisés

---

**Prêt à déployer, conforme aux standards d’équipe, pensé pour durer.**

---

*Besoin du README complet généré en markdown ? Ou du code starter ? Dis-le-moi, je peux te fournir le fichier prêt à déposer sur ton GitHub.*
