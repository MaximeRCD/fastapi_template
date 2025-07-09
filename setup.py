#!/usr/bin/env python3
"""Setup script for FastAPI Enterprise Template."""

import subprocess  # nosec B404
import sys
from pathlib import Path


def run_command(command: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command."""
    print(f"Running: {command}")
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True
    )  # nosec B602
    if check and result.returncode != 0:
        print(f"Error running command: {command}")
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        sys.exit(1)
    return result


def check_poetry() -> None:
    """Check if Poetry is installed."""
    result = run_command("poetry --version", check=False)
    if result.returncode != 0:
        print("Error: Poetry is not installed")
        print("Please install Poetry: https://python-poetry.org/docs/#installation")
        sys.exit(1)
    print("✓ Poetry detected")


def setup_environment() -> None:
    """Set up the development environment."""
    print("\n🚀 Setting up FastAPI Enterprise Template...")

    # Check prerequisites
    check_poetry()

    # Install dependencies
    print("\n📦 Installing dependencies...")
    run_command("poetry install")

    # Install pre-commit hooks
    print("\n🔧 Installing pre-commit hooks...")
    run_command("poetry run pre-commit install")

    # Create .env file if it doesn't exist
    env_file = Path(".env")
    env_example = Path("env.example")

    if not env_file.exists() and env_example.exists():
        print("\n📝 Creating .env file from template...")
        run_command(f"cp {env_example} .env")
        print("✓ .env file created (please update with your configuration)")

    # Initialize git if not already done
    if not Path(".git").exists():
        print("\n📝 Initializing git repository...")
        run_command("git init")
        run_command("git add .")
        run_command('git commit -m "Initial commit: FastAPI Enterprise Template"')

    print("\n✅ Setup complete!")
    print("\n📋 Next steps:")
    print("1. Update .env file with your configuration")
    print("2. Run 'make run' to start the development server")
    print("3. Visit http://localhost:8000/docs for API documentation")
    print("4. Run 'make test' to run tests")
    print("5. Run 'make lint' to check code quality")


if __name__ == "__main__":
    setup_environment()
