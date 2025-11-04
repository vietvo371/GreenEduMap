"""Initialize database - create tables."""

from app.db.base import engine, Base
from app.models import (
    AirQuality,
    School,
    EducationQuality,
    User,
    AIAnalysis,
)


def init_db():
    """Create all database tables."""
    print("🗄️  Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")


if __name__ == "__main__":
    init_db()
