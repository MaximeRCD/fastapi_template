"""Postal code CRUD operations."""

from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.postal_code import PostalCode


class CRUDPostalCode:
    """CRUD operations for PostalCode model."""

    async def get(self, db: AsyncSession, id: int) -> PostalCode | None:
        """Get postal code by ID."""
        result = await db.execute(select(PostalCode).where(PostalCode.id == id))
        postal_code = result.scalar_one_or_none()
        return (
            postal_code
            if isinstance(postal_code, PostalCode) or postal_code is None
            else None
        )

    async def get_by_postal_code(
        self, db: AsyncSession, postal_code: str
    ) -> PostalCode | None:
        """Get postal code by postal code string."""
        result = await db.execute(
            select(PostalCode).where(PostalCode.postal_code == postal_code)
        )
        postal_code_obj = result.scalar_one_or_none()
        return (
            postal_code_obj
            if isinstance(postal_code_obj, PostalCode) or postal_code_obj is None
            else None
        )

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> list[PostalCode]:
        """Get multiple postal codes."""
        result = await db.execute(select(PostalCode).offset(skip).limit(limit))
        return list(result.scalars().all())

    async def create(self, db: AsyncSession, *, obj_in: dict[str, Any]) -> PostalCode:
        """Create a new postal code."""
        db_obj = PostalCode(
            postal_code=obj_in["postal_code"],
            city_name=obj_in["city_name"],
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: AsyncSession, *, db_obj: PostalCode, obj_in: dict[str, Any]
    ) -> PostalCode:
        """Update a postal code."""
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, *, id: int) -> PostalCode | None:
        """Remove a postal code."""
        obj = await db.get(PostalCode, id)
        if obj:
            await db.delete(obj)
            await db.commit()
        return obj if isinstance(obj, PostalCode) or obj is None else None


postal_code = CRUDPostalCode()
