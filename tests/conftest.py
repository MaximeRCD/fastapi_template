"""Pytest configuration and fixtures."""

import asyncio
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.main import create_application


@pytest.fixture(scope="session")  # type: ignore
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture  # type: ignore
def app() -> FastAPI:
    """Create a FastAPI application for testing."""
    return create_application()


@pytest.fixture  # type: ignore
def client(app: FastAPI) -> Generator[TestClient, None, None]:
    """Create a test client for the FastAPI application."""
    with TestClient(app) as test_client:
        yield test_client


@pytest_asyncio.fixture  # type: ignore
async def async_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Create an async test client for the FastAPI application."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture  # type: ignore
def test_db_url() -> str:
    """Get test database URL."""
    return "sqlite+aiosqlite:///./test.db"


@pytest_asyncio.fixture  # type: ignore
async def test_db_session(test_db_url: str) -> AsyncGenerator[AsyncSession, None]:
    """Create a test database session."""
    engine = create_async_engine(
        test_db_url,
        echo=False,
    )

    async_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest.fixture  # type: ignore
def override_get_db(
    test_db_session: AsyncSession,
) -> Generator[AsyncSession, None, None]:
    """Override the database dependency for testing."""

    async def _override_get_db() -> AsyncSession:
        yield test_db_session

    return _override_get_db  # type: ignore
