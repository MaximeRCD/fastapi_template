# Contributing to FastAPI Enterprise Template

Welcome! 🚀 Thank you for your interest in contributing to our FastAPI Enterprise Template. This guide will help you get started with local development, Docker setup, and the contribution workflow.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.12+** - [Download here](https://www.python.org/downloads/)
- **Poetry** - [Installation guide](https://python-poetry.org/docs/#installation)
- **Git** - [Download here](https://git-scm.com/downloads)
- **Docker & Docker Compose** - [Installation guide](https://docs.docker.com/get-docker/)

---

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

Run our setup script to automatically configure everything:

```bash
python setup.py
```

This will:
- ✅ Check Python version (3.12+)
- ✅ Verify Poetry installation
- ✅ Install all dependencies
- ✅ Set up pre-commit hooks
- ✅ Create `.env` file from template
- ✅ Initialize git repository (if needed)

### Option 2: Manual Setup

If you prefer manual setup:

```bash
# 1. Install dependencies
poetry install

# 2. Install pre-commit hooks
poetry run pre-commit install

# 3. Create environment file
cp env.example .env

# 4. Start development server
make run
```

---

## 🐳 Docker Development

### Using Docker Compose (Recommended for Development)

Our Docker Compose setup includes PostgreSQL and Redis:

```bash
# Start all services (app, database, redis)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and start
docker-compose up -d --build
```

### Using Docker Only

```bash
# Build the image
docker build -t fastapi-enterprise-template .

# Run the container
docker run -p 8000:8000 fastapi-enterprise-template
```

---

## 🛠️ Development Workflow

### 1. Environment Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/fastapi-enterprise-template.git
   cd fastapi-enterprise-template
   ```

2. **Set up your environment:**
   ```bash
   python setup.py
   ```

3. **Update configuration:**
   - Edit `.env` file with your settings
   - Update database URL if needed

### 2. Running the Application

#### Local Development
```bash
# Start development server
make run

# Or with Poetry
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Docker Development
```bash
# Start with database
docker-compose up -d

# View logs
docker-compose logs -f app
```

### 3. Accessing the Application

- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **API Health**: http://localhost:8000/api/v1/health/

---

## 🧪 Testing & Quality Assurance

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run tests in watch mode
make test-watch

# Run specific test file
poetry run pytest tests/test_main.py

# Run tests with specific marker
poetry run pytest -m "slow"
```

### Code Quality Checks

```bash
# Run all quality checks
make check-all

# Individual checks
make lint      # Ruff, Flake8, Bandit
make format    # Black, isort
make typecheck # mypy
make security  # Bandit, safety
```

### Pre-commit Hooks

```bash
# Install hooks (done automatically by setup.py)
poetry run pre-commit install

# Run hooks on all files
make pre-commit

# Run specific hook
poetry run pre-commit run black --all-files
```

---

## 📝 Contribution Workflow

### 1. Before You Start

- [ ] **Create an issue** for your feature/bug fix
- [ ] **Discuss the approach** with the team
- [ ] **Plan your changes** and impact on architecture

### 2. Development Setup

```bash
# 1. Create feature branch
git checkout -b feature/your-feature-name

# 2. Ensure you're up to date
git pull origin main

# 3. Set up your environment
python setup.py
```

### 3. Development Process

#### Writing Code
- ✅ Use **async/await** for all I/O operations
- ✅ Add **type hints** to all functions
- ✅ Write **docstrings** for all functions/classes
- ✅ Follow **PEP 8** and our linting rules

#### Database Changes
```bash
# Create new migration
make migrate-create name=add_user_table

# Apply migrations
make migrate
```

#### Testing
- ✅ Write **unit tests** for new functions
- ✅ Write **integration tests** for new endpoints
- ✅ Maintain **>90% test coverage**
- ✅ Test **edge cases** and error scenarios

### 4. Quality Gates

Before submitting your PR, ensure:

```bash
# 1. Run all quality checks
make check-all

# 2. Run tests with coverage
make test-cov

# 3. Check if coverage is >90%
poetry run pytest --cov=app --cov-report=term-missing

# 4. Run pre-commit hooks
make pre-commit
```

### 5. Pull Request Process

1. **Create PR** with descriptive title and description
2. **Link to issue** using `Fixes #123` or `Closes #123`
3. **Fill out PR template** completely
4. **Add screenshots/logs** for visual changes
5. **Tag reviewers** appropriately

### 6. PR Checklist

- [ ] **Tests pass** with >90% coverage
- [ ] **Linting passes** (Black, Ruff, Flake8)
- [ ] **Type checking passes** (mypy)
- [ ] **Security checks pass** (Bandit)
- [ ] **Documentation updated**
- [ ] **No breaking changes** (or clearly documented)
- [ ] **Database migrations** included (if needed)

---

## 🏗️ Project Structure

```
fastapi-enterprise-template/
├── app/                    # Main application
│   ├── api/               # API endpoints
│   │   └── v1/           # API version 1
│   ├── core/              # Core functionality
│   │   ├── config.py     # Settings
│   │   └── logging.py    # Logging setup
│   ├── db/               # Database layer
│   │   ├── base.py       # Database setup
│   │   └── base_class.py # Base model
│   ├── models/           # SQLAlchemy models
│   └── main.py           # Application entry
├── tests/                # Test suite
├── migrations/           # Database migrations
├── docs/                # Documentation
└── .github/             # CI/CD workflows
```

---

## 🛠️ Available Commands

### Development
```bash
make run          # Start development server
make run-prod     # Start production server
make test         # Run tests
make test-cov     # Run tests with coverage
make lint         # Run linting
make format       # Format code
make typecheck    # Run type checking
make security     # Run security checks
```

### Docker
```bash
make docker-build # Build Docker image
make docker-run   # Start with Docker Compose
make docker-stop  # Stop Docker Compose
make docker-logs  # View Docker logs
```

### Database
```bash
make migrate           # Apply migrations
make migrate-create    # Create new migration
```

### Documentation
```bash
make docs         # Build documentation
make serve-docs   # Serve documentation locally
```

### Maintenance
```bash
make clean        # Clean generated files
make upgrade-deps # Upgrade dependencies
make help         # Show all commands
```

---

## 🐛 Troubleshooting

### Common Issues

#### Poetry Issues
```bash
# Clear Poetry cache
poetry cache clear . --all

# Reinstall dependencies
poetry install --sync
```

#### Database Issues
```bash
# Reset database (Docker)
docker-compose down -v
docker-compose up -d

# Reset migrations
rm -rf migrations/versions/*
alembic revision --autogenerate -m "initial"
```

#### Pre-commit Issues
```bash
# Update pre-commit hooks
poetry run pre-commit autoupdate

# Skip hooks temporarily
git commit -m "message" --no-verify
```

#### Docker Issues
```bash
# Clean Docker
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache
```

---

## 📚 Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **SQLAlchemy Documentation**: https://docs.sqlalchemy.org/
- **Pytest Documentation**: https://docs.pytest.org/
- **Poetry Documentation**: https://python-poetry.org/docs/
- **Docker Documentation**: https://docs.docker.com/

---

## 🤝 Getting Help

- **Create an issue** for bugs or feature requests
- **Join our discussions** for questions and ideas
- **Check existing issues** before creating new ones
- **Use the search** to find similar problems

---

## 📄 Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to keep our community approachable and respectable.

---

**Thank you for contributing to FastAPI Enterprise Template!** 🎉

Your contributions help make this project better for everyone. If you have any questions or need help, don't hesitate to reach out.
