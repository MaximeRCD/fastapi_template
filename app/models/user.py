"""User model."""

from sqlalchemy import Boolean, Column, String

from app.db.base_class import Base


class User(Base):
    """User model for database."""

    __tablename__ = "users"  # type: ignore

    # User fields
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    def __repr__(self) -> str:
        """String representation of User."""
        return f"<User(id={self.id}, email='{self.email}')>"
