Here’s a deduplicated, concise, and fully translated English version of your README, merging and streamlining all key points and recommendations.
Unnecessary repetitions and explanations about Python 3.12 or tool choices have been grouped under single sections.

---

# FASTAPI Enterprise Template

🚀 **FastAPI Enterprise Template** — Python 3.12+
A robust, professional-grade FastAPI boilerplate, optimized for Python 3.12+. Ideal for launching new web services in an enterprise setting where code quality, speed, and maintainability are essential.

---

## Overview

This project provides a **modern and reliable FastAPI foundation**, fully leveraging the latest features and performance improvements from **Python 3.12**. All dependencies and tools are tested and strictly compatible with Python 3.12.

---

## Highlights & Features

* **Full Python 3.12 support**: Strict dependency management and CI/CD pipelines guarantee 3.12 compatibility.
* **Modern Python features**: Advanced pattern matching, new type hints (`Self`, `Any`, etc.), and improved performance.
* **Professional architecture**: Scalable, microservices-ready codebase.
* **Dependency management**: [Poetry](https://python-poetry.org/), with Python 3.12+ enforced.
* **Best-in-class tooling**:

  * **Linting/Formatting/Type Checking**: Black, Ruff, isort, Flake8, mypy.
  * **Testing**: pytest, pytest-cov, pytest-asyncio for async code.
  * **Pre-commit hooks**: Formatting, lint, security checks.
* **CI/CD**: GitHub Actions pipelines (lint, test, coverage, docs, security).
* **Interactive API docs**: Swagger (OpenAPI), Redoc; project docs via mkdocs.
* **Structured logging**: structlog/loguru.
* **Modern configuration**: dotenv + Pydantic v2+.
* **Security**: Bandit, dependency checks.
* **Makefile** utilities.
* **Docker & Docker Compose**: Production and development-ready with live reloading.

---

## Project Structure

```
fastapi-enterprise-template/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── crud/
│   ├── db/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
├── tests/
├── scripts/
├── migrations/
├── .github/
│   └── workflows/
├── .env.example
├── .pre-commit-config.yaml
├── pyproject.toml
├── Makefile
├── README.md
├── mkdocs.yml
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
└── LICENSE
```

---

## Dependencies & Tooling (Python 3.12+ compatible)

* **Poetry** (`pyproject.toml` defines `python = "^3.12"`)
* **FastAPI**, **Uvicorn**
* **Pydantic v2+**
* **SQLAlchemy 2.0+**, **asyncpg**
* **Black**, **isort**, **Ruff**, **Flake8**
* **pytest**, **pytest-cov**, **pytest-asyncio**
* **mypy**
* **Bandit**
* **pre-commit**
* **mkdocs**
* **alembic** (for migrations)

---

## Installation & Quickstart

### Local Development

```bash
# Clone the repo and set up Python 3.12+
git clone https://github.com/your-org/fastapi-enterprise-template.git
cd fastapi-enterprise-template

# Install dependencies with Poetry (will check Python version)
poetry install

# Copy the environment file
cp .env.example .env

# Run the API (development)
make run

# Access API docs: http://localhost:8000/docs
```

### Docker Development (Recommended)

```bash
# Clone the repo
git clone https://github.com/your-org/fastapi-enterprise-template.git
cd fastapi-enterprise-template

# Start the development environment with live reloading
make docker-dev

# Or run in background
make docker-run

# View logs
make docker-logs

# Access API docs: http://localhost:8000/docs
```

#### Docker Development Features

* **Live code reloading**: Changes to your code automatically restart the server
* **Real PostgreSQL database**: No more mock data, full database integration
* **Isolated environment**: Consistent development environment across team members
* **Health checks**: Automatic monitoring of services
* **Easy database access**: `make docker-db-shell` to connect to PostgreSQL

#### Docker Commands

```bash
# Development with logs
make docker-dev

# Run in background
make docker-run

# Stop services
make docker-stop

# View logs
make docker-logs
make docker-logs-app
make docker-logs-db

# Access container shells
make docker-shell
make docker-db-shell

# Database operations
make docker-migrate
make docker-db-init

# Run tests in container
make docker-test

# Clean up everything
make docker-clean
```

---

## Linting, Pre-commit, Tests

```bash
# Install pre-commit hooks (required for all contributors)
poetry run pre-commit install

# Run linting, formatting, type checks
make lint
make format
make typecheck

# Run tests
make test
```

---

## Database Operations

### Local Development

```bash
# Initialize database tables
make db-init

# Run migrations
make migrate

# Create new migration
make migrate-create name=add_new_field
```

### Docker Development

```bash
# Initialize database in Docker
make docker-db-init

# Run migrations in Docker
make docker-migrate

# Create new migration in Docker
make docker-migrate-create name=add_new_field
```

---

## API Endpoints

The application includes a complete User management system with real database integration:

* `GET /api/v1/users/` - List all users
* `GET /api/v1/users/{user_id}` - Get specific user
* `POST /api/v1/users/` - Create new user
* `PUT /api/v1/users/{user_id}` - Update user
* `DELETE /api/v1/users/{user_id}` - Delete user

All endpoints use real PostgreSQL database operations with proper error handling and validation.

---

## CI/CD

* **GitHub Actions** pipeline for Python 3.12: lint, tests, coverage, security, docs.
* **Build badge** included in README.
* **Easily adaptable** to other CI tools.

---

## Documentation

* **API**: Swagger (OpenAPI) and Redoc via FastAPI.
* **Project docs**: mkdocs, Markdown-based, easy to host.
* **Type hints** throughout the codebase (take advantage of Python 3.12 improvements).

---

## Why Python 3.12?

* **Better performance** (optimized CPython)
* **New native types** (`Self`, `typing.Any`, etc.)
* **Advanced pattern matching**
* **Modern standard library APIs**
* **Long-term support and security**

---

## Enterprise Usage Tips

* **Always use a local Python 3.12 virtual environment per project.**
* **Keep dependencies up to date** (`make upgrade-deps`).
* **Check library compatibility with Python 3.12 before upgrading.**
* **Enforce code reviews, aim for >90% test coverage.**
* **Require docs and tests for every feature.**
* **Deploy only on Python 3.12 environments (recommended Docker base: `python:3.12-slim`).**
* **Use Docker for development** to ensure consistent environments across team members.

---

## Example: `pyproject.toml`

```toml
[tool.poetry]
name = "fastapi-enterprise-template"
version = "0.1.0"
description = "FastAPI starter template for enterprise (Python 3.12+)"
authors = ["Your Name <your@email.com>"]
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

---

## Recommended Advanced Practices

### Issue and Pull Request Templates

**Purpose:** Standardize contributions, improve tracking and review quality.
**How:**

* Add files in `.github/ISSUE_TEMPLATE/` for bug reports, improvements, docs, questions.
* Create `.github/pull_request_template.md` to guide PRs (description, checklist, test/lint, breaking changes, etc.).

**Example:**

```markdown
## PR Objective

## Summary of changes

## Checklist
- [ ] Lint/Format OK
- [ ] Tests passing
- [ ] Docs updated
- [ ] No unintended breaking changes
- [ ] Linked to issue? (ref)

## Screenshots/Logs
```

---

### Docker Best Practices

* **Base image:** `python:3.12-slim`
* **Dependency management:** Use Poetry.
* **Small images:** Install minimal system deps, clean pip/apt cache.
* **Proper `.dockerignore`:** Exclude tests, venv, cache, etc.

**Minimal Dockerfile:**

```dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.3
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --only main

COPY app ./app
COPY alembic.ini .
COPY migrations ./migrations

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Example `.dockerignore`:**

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
docker-compose.yml
alembic.ini
migrations/
*.db
```

**Example `docker-compose.yml`:**

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
      - ./app:/app/app
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

### Database Migrations (SQLAlchemy 2.0+ & Alembic)

* **Use Alembic** for database schema migrations.
* **Always review auto-generated migration diffs!**
* **Version-control the `migrations/` folder.**
* **Add Makefile shortcuts** for migration commands.

**Makefile Example:**

```makefile
migrate:
	poetry run alembic revision --autogenerate -m "Migration"

upgrade:
	poetry run alembic upgrade head

downgrade:
	poetry run alembic downgrade -1
```

---

### Optimized Async Services (FastAPI & Python 3.12)

* Use `async/await` everywhere possible: endpoints, services, DB (with async SQLAlchemy), external APIs (httpx).
* Prefer async clients for DB and HTTP.

**Example async service:**

```python
from app.db.session import async_session
from app.models.user import User
from sqlalchemy import select

async def get_user_by_email(email: str) -> User | None:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
```

**Example async test (pytest-asyncio):**

```python
import pytest
from app.services.user_service import get_user_by_email

@pytest.mark.asyncio
async def test_get_user_by_email():
    user = await get_user_by_email("test@example.com")
    assert user is None or user.email == "test@example.com"
```

---

## Appendix: Useful Links

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Pydantic v2 Docs](https://docs.pydantic.dev/latest/)
* [SQLAlchemy AsyncIO](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
* [Alembic for SQLAlchemy 2.0](https://alembic.sqlalchemy.org/en/latest/changelog.html#version-1-10-0)
* [Poetry Docs](https://python-poetry.org/docs/)
* [pytest-asyncio](https://pytest-asyncio.readthedocs.io/en/latest/)
* [mkdocs](https://www.mkdocs.org/)

---

*Ready to build robust, modern FastAPI services with the best practices and performance of Python 3.12!*

---

If you need any code sample or file from the original template, just ask!
