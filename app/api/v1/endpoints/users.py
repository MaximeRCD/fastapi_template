"""User endpoints."""

from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from structlog import get_logger

logger = get_logger(__name__)
router = APIRouter()


class UserBase(BaseModel):
    """Base user model."""

    email: str
    full_name: str | None = None
    is_active: bool = True


class UserCreate(UserBase):
    """User creation model."""

    password: str


class UserResponse(UserBase):
    """User response model."""

    id: int

    class Config:
        from_attributes = True


# Mock data for demonstration
mock_users = [
    {
        "id": 1,
        "email": "admin@example.com",
        "full_name": "Admin User",
        "is_active": True,
    },
    {
        "id": 2,
        "email": "user@example.com",
        "full_name": "Regular User",
        "is_active": True,
    },
]


@router.get("/", response_model=list[UserResponse])  # type: ignore
async def get_users() -> list[dict[str, Any]]:
    """Get all users."""
    logger.info("Retrieving all users")
    return mock_users


@router.get("/{user_id}", response_model=UserResponse)  # type: ignore
async def get_user(user_id: int) -> dict[str, Any]:
    """Get a specific user by ID."""
    logger.info("Retrieving user", user_id=user_id)

    for user in mock_users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )


@router.post(
    "/", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)  # type: ignore
async def create_user(user: UserCreate) -> dict[str, Any]:
    """Create a new user."""
    logger.info("Creating new user", email=user.email)

    # Mock user creation
    new_user = {
        "id": len(mock_users) + 1,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active,
    }

    mock_users.append(new_user)
    return new_user
