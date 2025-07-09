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

docker-build: ## Build Docker image
	docker build -t fastapi-enterprise-template .

docker-run: ## Run with Docker Compose
	docker-compose up -d

docker-stop: ## Stop Docker Compose services
	docker-compose down

docker-logs: ## View Docker Compose logs
	docker-compose logs -f

docs: ## Build documentation
	poetry run mkdocs build

serve-docs: ## Serve documentation locally
	poetry run mkdocs serve

migrate: ## Run database migrations
	poetry run alembic upgrade head

migrate-create: ## Create a new migration (usage: make migrate-create name=migration_name)
	poetry run alembic revision --autogenerate -m "$(name)"

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
