"""SQLAlchemy engine, session factory, and declarative base."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///./security_demo.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)
SESSION_FACTORY = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# SQLAlchemy models declare data fields; behavior is supplied by the ORM.
class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Base class for declarative database models."""
