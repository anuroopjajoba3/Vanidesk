"""The connection to the SQLite database."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

# SQLite normally refuses to be used from more than one thread. FastAPI runs
# routes in a thread pool, so this check has to be switched off.
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Every model (table) inherits from this class."""


def create_tables():
    """Create any table that does not exist yet. Existing tables are left alone."""
    # The import registers the models on Base. Without it, Base knows no tables.
    from app.db import models  # noqa: F401

    Base.metadata.create_all(engine)


def get_db():
    """Give a route a database session, and close it when the route is done."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
