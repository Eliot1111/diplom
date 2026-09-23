"""Persistent users and items."""

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


# SQLAlchemy models declare data fields; behavior is supplied by the ORM.
class User(Base):  # pylint: disable=too-few-public-methods
    """A user account with a password hash and an authorization role."""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), default="user")

    items: Mapped[list["Item"]] = relationship(back_populates="owner")


# SQLAlchemy models declare data fields; behavior is supplied by the ORM.
class Item(Base):  # pylint: disable=too-few-public-methods
    """An item associated with its owner."""
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner: Mapped[User] = relationship(back_populates="items")
