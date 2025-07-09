"""FastAPI Enterprise Template Main Application."""

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from structlog import get_logger

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logging import setup_logging

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """Application lifespan manager."""
    # Startup
    logger.info("Starting FastAPI Enterprise Template application")
    setup_logging()

    yield

    # Shutdown
    logger.info("Shutting down FastAPI Enterprise Template application")


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.APP_VERSION,
        description=(
            "A robust, professional-grade FastAPI boilerplate for enterprise applications"
        ),
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL,
        lifespan=lifespan,
    )

    # Set up CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.ALLOWED_CREDENTIALS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API router
    app.include_router(api_router, prefix=settings.API_V1_STR)

    @app.exception_handler(Exception)  # type: ignore
    async def global_exception_handler(
        request: Request, exc: Exception
    ) -> JSONResponse:
        """Global exception handler."""
        logger.error(
            "Unhandled exception",
            exc_info=exc,
            path=request.url.path,
        )  # noqa: E501
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )

    @app.get("/")  # type: ignore
    async def root() -> dict[str, str]:
        """Root endpoint."""
        return {"message": "Welcome to FastAPI Enterprise Template"}

    @app.get("/health")  # type: ignore
    async def health_check() -> dict[str, str]:
        """Health check endpoint."""
        return {"status": "healthy"}

    return app


app = create_application()
