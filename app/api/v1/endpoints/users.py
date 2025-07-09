"""User endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from app.crud.user import user
from app.db.base import get_db
from app.models.user import User

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


@router.get("/", response_model=list[UserResponse])  # type: ignore
async def get_users(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> list[User]:
    """Get all users."""
    logger.info("Retrieving all users", skip=skip, limit=limit)
    users = await user.get_multi(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserResponse)  # type: ignore
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)) -> User:
    """Get a specific user by ID."""
    logger.info("Retrieving user", user_id=user_id)

    db_user = await user.get(db, id=user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return db_user


@router.post(
    "/", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)  # type: ignore
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)) -> User:
    """Create a new user."""
    logger.info("Creating new user", email=user_in.email)

    # Check if user already exists
    existing_user = await user.get_by_email(db, email=user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )

    # Create user data dict
    user_data = {
        "email": user_in.email,
        "password": user_in.password,
        "full_name": user_in.full_name,
        "is_active": user_in.is_active,
    }

    db_user = await user.create(db, obj_in=user_data)
    return db_user


@router.put("/{user_id}", response_model=UserResponse)  # type: ignore
async def update_user(
    user_id: int,
    user_in: UserBase,
    db: AsyncSession = Depends(get_db),
) -> User:
    """Update a user."""
    logger.info("Updating user", user_id=user_id)

    db_user = await user.get(db, id=user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # Check if email is being changed and if it already exists
    if user_in.email != db_user.email:
        existing_user = await user.get_by_email(db, email=user_in.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists",
            )

    user_data = user_in.model_dump(exclude_unset=True)
    db_user = await user.update(db, db_obj=db_user, obj_in=user_data)
    return db_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)  # type: ignore[misc]
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)) -> None:
    """Delete a user."""
    logger.info("Deleting user", user_id=user_id)

    db_user = await user.get(db, id=user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    await user.remove(db, id=user_id)
