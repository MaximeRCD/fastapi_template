"""User CRUD operations."""

from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash, verify_password
from app.models.user import User


class CRUDUser:
    """CRUD operations for User model."""

    async def get(self, db: AsyncSession, id: int) -> User | None:
        """Get user by ID."""
        result = await db.execute(select(User).where(User.id == id))
        user = result.scalar_one_or_none()
        return user if isinstance(user, User) or user is None else None

    async def get_by_email(self, db: AsyncSession, email: str) -> User | None:
        """Get user by email."""
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        return user if isinstance(user, User) or user is None else None

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> list[User]:
        """Get multiple users."""
        result = await db.execute(select(User).offset(skip).limit(limit))
        return list(result.scalars().all())

    async def create(self, db: AsyncSession, *, obj_in: dict[str, Any]) -> User:
        """Create a new user."""
        db_obj = User(
            email=obj_in["email"],
            hashed_password=get_password_hash(obj_in["password"]),
            full_name=obj_in.get("full_name"),
            is_active=obj_in.get("is_active", True),
            is_superuser=obj_in.get("is_superuser", False),
            address=obj_in.get("address"),
            age=obj_in.get("age"),
            postal_code_id=obj_in.get("postal_code_id"),
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: AsyncSession, *, db_obj: User, obj_in: dict[str, Any]
    ) -> User:
        """Update a user."""
        for field, value in obj_in.items():
            if field == "password":
                hashed_password = get_password_hash(value)
                db_obj.hashed_password = hashed_password
            else:
                setattr(db_obj, field, value)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, *, id: int) -> User | None:
        """Remove a user."""
        obj = await db.get(User, id)
        if obj:
            await db.delete(obj)
            await db.commit()
        return obj if isinstance(obj, User) or obj is None else None

    async def authenticate(
        self, db: AsyncSession, *, email: str, password: str
    ) -> User | None:
        """Authenticate a user."""
        user = await self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def is_active(self, user: User) -> bool:
        """Check if user is active."""
        return bool(user.is_active)

    async def is_superuser(self, user: User) -> bool:
        """Check if user is superuser."""
        return bool(user.is_superuser)


user = CRUDUser()
