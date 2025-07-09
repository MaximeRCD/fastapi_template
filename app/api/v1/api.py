"""Main API router for v1 endpoints."""

from fastapi import APIRouter

from app.api.v1.endpoints import health, postal_codes, users

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    postal_codes.router, prefix="/postal-codes", tags=["postal-codes"]
)
