.PHONY: help install install-dev run test lint format typecheck clean docker-build docker-run docker-stop docs serve-docs upgrade-deps

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	poetry install --only main

install-dev: ## Install all dependencies (including dev)
	poetry install
	poetry run pre-commit install

run: ## Run the FastAPI application in development mode
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

run-prod: ## Run the FastAPI application in production mode
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

test: ## Run tests with coverage
	poetry run pytest

test-watch: ## Run tests in watch mode
	poetry run pytest-watch

test-cov: ## Run tests with coverage report
	poetry run pytest --cov=app --cov-report=html --cov-report=term-missing

lint: ## Run all linting tools
	poetry run ruff check .
	poetry run flake8 app tests
	poetry run bandit -r app

format: ## Format code with black and isort
	poetry run black .
	poetry run isort .

format-check: ## Check if code is formatted correctly
	poetry run black --check .
	poetry run isort --check-only .

typecheck: ## Run type checking with mypy
	poetry run mypy app

security: ## Run security checks
	poetry run bandit -r app
	poetry run safety check

pre-commit: ## Run pre-commit hooks on all files
	poetry run pre-commit run --all-files

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .coverage htmlcov .pytest_cache .mypy_cache

# Docker Development Commands
docker-build: ## Build Docker image
	docker build -t fastapi-enterprise-template .

docker-run: ## Run with Docker Compose
	docker-compose up -d

docker-dev: ## Run with Docker Compose in development mode (with logs)
	docker-compose up

docker-stop: ## Stop Docker Compose services
	docker-compose down

docker-logs: ## View Docker Compose logs
	docker-compose logs -f

docker-logs-app: ## View only app logs
	docker-compose logs -f app

docker-logs-db: ## View only database logs
	docker-compose logs -f db

docker-restart: ## Restart Docker Compose services
	docker-compose restart

docker-clean: ## Stop and remove all containers, networks, and volumes
	docker-compose down -v --remove-orphans

docker-shell: ## Access app container shell
	docker-compose exec app bash

docker-db-shell: ## Access database container shell
	docker-compose exec db psql -U postgres -d fastapi_enterprise

docker-migrate: ## Run migrations in Docker container
	docker-compose exec app poetry run alembic upgrade head

docker-migrate-create: ## Create a new migration in Docker container (usage: make docker-migrate-create name=migration_name)
	docker-compose exec app poetry run alembic revision --autogenerate -m "$(name)"

docker-test: ## Run tests in Docker container
	docker-compose exec app poetry run pytest

docker-lint: ## Run linting in Docker container
	docker-compose exec app poetry run ruff check .

# Database Commands
migrate: ## Run database migrations
	poetry run alembic upgrade head

migrate-create: ## Create a new migration (usage: make migrate-create name=migration_name)
	poetry run alembic revision --autogenerate -m "$(name)"

db-init: ## Initialize database (create tables)
	poetry run python -c "from app.db.base import init_db; import asyncio; asyncio.run(init_db())"

docker-db-init: ## Initialize database in Docker container
	docker-compose exec app poetry run python -c "from app.db.base import init_db; import asyncio; asyncio.run(init_db())"

docs: ## Build documentation
	poetry run mkdocs build

serve-docs: ## Serve documentation locally
	poetry run mkdocs serve

upgrade-deps: ## Upgrade all dependencies
	poetry update

check-all: ## Run all checks (lint, format, typecheck, test)
	$(MAKE) lint
	$(MAKE) format-check
	$(MAKE) typecheck
	$(MAKE) test

ci: ## Run CI checks (used in GitHub Actions)
	$(MAKE) install-dev
	$(MAKE) check-all
	$(MAKE) security
	$(MAKE) docs
