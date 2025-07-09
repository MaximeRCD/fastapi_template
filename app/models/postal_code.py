"""Postal code model."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class PostalCode(Base):
    """Postal code model for database."""

    __tablename__ = "postal_codes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    postal_code: Mapped[str] = mapped_column(
        String, unique=True, nullable=False, index=True
    )
    city_name: Mapped[str] = mapped_column(String, nullable=False)

    # Relationship to users
    users = relationship("User", back_populates="postal_code")

    def __repr__(self) -> str:
        """String representation of PostalCode."""
        return f"<PostalCode(id={self.id}, postal_code='{self.postal_code}', city_name='{self.city_name}')>"
