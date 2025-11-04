
from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # FastAPI
    app_name: str = "GreenEduMap API"
    app_version: str = "1.0.0"
    debug: bool = os.getenv("DEBUG", "True").lower() == "true"

    # Server
    api_prefix: str = "/api"

    # Security
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Database
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres:password@localhost:5432/greenedumap"
    )

    # CORS
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:8000",
        "*",  # Allow all origins in development
    ]

    # External APIs
    openaq_api_key: str = os.getenv("OPENAQ_API_KEY", "demo")
    openaq_api_url: str = "https://api.openaq.org/v2"

    openweather_api_key: str = os.getenv("OPENWEATHER_API_KEY", "demo")
    openweather_api_url: str = "https://api.openweathermap.org/data/2.5"

    # FiWARE Orion-LD
    orion_url: str = os.getenv("ORION_URL", "http://localhost:1026")
    orion_version: str = "v1"

    # MongoDB
    mongo_url: str = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    mongo_db: str = "orion"

    # Logging
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    # AI
    ai_correlation_threshold: float = 0.5
    ai_cluster_count: int = 5

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
