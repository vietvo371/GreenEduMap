from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.debug,
    connect_args={
        "connect_timeout": 10,
    } if "postgresql" in settings.DATABASE_URL else {}
)

# Create session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# Create base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    """Get database session for endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
