"""Postal code endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from app.crud.postal_code import postal_code
from app.db.base import get_db
from app.models.postal_code import PostalCode

logger = get_logger(__name__)
router = APIRouter()


class PostalCodeResponse(BaseModel):
    """Postal code response model."""

    id: int
    postal_code: str
    city_name: str

    class Config:
        from_attributes = True


@router.get("/", response_model=list[PostalCodeResponse])  # type: ignore
async def get_postal_codes(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> list[PostalCode]:
    """Get all Parisian postal codes."""
    logger.info("Retrieving all Parisian postal codes", skip=skip, limit=limit)
    postal_codes = await postal_code.get_multi(db, skip=skip, limit=limit)
    return postal_codes


@router.get("/{postal_code_id}", response_model=PostalCodeResponse)  # type: ignore
async def get_postal_code(
    postal_code_id: int, db: AsyncSession = Depends(get_db)
) -> PostalCode:
    """Get a specific postal code by ID."""
    logger.info("Retrieving postal code", postal_code_id=postal_code_id)

    db_postal_code = await postal_code.get(db, id=postal_code_id)
    if not db_postal_code:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Postal code not found",
        )
    return db_postal_code


@router.get("/by-code/{postal_code_str}", response_model=PostalCodeResponse)  # type: ignore
async def get_postal_code_by_code(
    postal_code_str: str, db: AsyncSession = Depends(get_db)
) -> PostalCode:
    """Get a specific postal code by postal code string."""
    logger.info("Retrieving postal code by code", postal_code=postal_code_str)

    db_postal_code = await postal_code.get_by_postal_code(
        db, postal_code=postal_code_str
    )
    if not db_postal_code:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Postal code not found",
        )
    return db_postal_code
