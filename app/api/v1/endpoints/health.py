"""Health check endpoints."""

from datetime import datetime
from typing import Any

from fastapi import APIRouter
from structlog import get_logger

from app.core.config import settings

logger = get_logger(__name__)
router = APIRouter()


@router.get("/")  # type: ignore
async def health_check() -> dict[str, Any]:
    """Basic health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@router.get("/detailed")  # type: ignore
async def detailed_health_check() -> dict[str, Any]:
    """Detailed health check with system information."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "app_name": settings.APP_NAME,
        "debug": settings.DEBUG,
        "database_url": (
            settings.DATABASE_URL.split("@")[-1]
            if "@" in settings.DATABASE_URL
            else "configured"
        ),
        "cors_enabled": bool(settings.ALLOWED_ORIGINS),
        "redis_configured": bool(settings.REDIS_URL),
    }
