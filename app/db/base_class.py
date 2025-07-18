"""Base class for SQLAlchemy models."""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all database models."""

    # Common fields for all models
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
