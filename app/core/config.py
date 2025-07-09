"""Application configuration using Pydantic Settings."""

import json
from typing import Any

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings using Pydantic Settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application Settings
    APP_NAME: str = "FastAPI Enterprise Template"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"

    # Server Settings
    HOST: str = "127.0.0.1"  # nosec B104
    PORT: int = 8000
    WORKERS: int = 1

    # Database Settings
    DATABASE_URL: str = (
        "postgresql+asyncpg://user:password@localhost:5432/fastapi_enterprise"
    )
    DATABASE_ECHO: bool = False

    # Security Settings
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS Settings
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]
    ALLOWED_CREDENTIALS: bool = True

    # Logging Settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Enterprise Template"

    # Documentation Settings
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"

    # Redis Settings (optional)
    REDIS_URL: str | None = None

    # Email Settings (optional)
    SMTP_TLS: bool = True
    SMTP_PORT: int = 587
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""

    # External APIs (optional)
    EXTERNAL_API_URL: str = "https://api.example.com"
    EXTERNAL_API_KEY: str = ""

    # Monitoring (optional)
    SENTRY_DSN: str | None = None
    PROMETHEUS_MULTIPROC_DIR: str = "/tmp"  # nosec B108

    @field_validator("ALLOWED_ORIGINS", mode="before")  # type: ignore
    @classmethod
    def parse_allowed_origins(cls, v: Any) -> list[str]:
        """Parse ALLOWED_ORIGINS from string to list."""
        if isinstance(v, str):
            try:
                parsed = json.loads(v)
                if isinstance(parsed, list):
                    return parsed
                return [v]
            except json.JSONDecodeError:
                return [v]
        if isinstance(v, list):
            return v
        return [str(v)]

    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.ENVIRONMENT.lower() == "development"

    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.ENVIRONMENT.lower() == "production"

    @property
    def is_testing(self) -> bool:
        """Check if running in testing mode."""
        return self.ENVIRONMENT.lower() == "testing"


# Global settings instance
settings = Settings()
