
from pydantic_settings import BaseSettings
from pydantic import ConfigDict, Field
from typing import List

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # FastAPI
    app_name: str = "GreenEduMap API"
    app_version: str = "1.0.0"
    debug: bool = False

    # Server
    api_prefix: str = "/api"

    # Security
    secret_key: str = Field(default="your-secret-key-change-in-production", alias="SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Database
    database_url: str = Field(
        default="postgresql+psycopg2://postgres:password@localhost:5432/greenedumap",
        alias="DATABASE_URL"
    )

    # CORS - keep as string to avoid JSON parsing issues
    cors_origins: str = Field(
        default="http://localhost:3000,http://localhost:3001,*",
        alias="CORS_ORIGINS"
    )

    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS origins string to list."""
        if isinstance(self.cors_origins, str):
            return [origin.strip() for origin in self.cors_origins.split(",")]
        return self.cors_origins if isinstance(self.cors_origins, list) else []

    # External APIs
    openaq_api_key: str = Field(default="demo", alias="OPENAQ_API_KEY")
    openaq_api_url: str = "https://api.openaq.org/v2"

    openweather_api_key: str = Field(default="demo", alias="OPENWEATHER_API_KEY")
    openweather_api_url: str = "https://api.openweathermap.org/data/2.5"

    # FiWARE Orion-LD
    orion_url: str = Field(default="http://localhost:1026", alias="ORION_URL")
    orion_version: str = "v1"

    # MongoDB
    mongo_url: str = Field(default="mongodb://localhost:27017", alias="MONGO_URL")
    mongo_db: str = "orion"

    # Logging
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    # AI
    ai_correlation_threshold: float = 0.5
    ai_cluster_count: int = 5

    model_config = ConfigDict(
        extra='ignore',
        env_file='.env',
        case_sensitive=False,
        populate_by_name=True
    )

settings = Settings()
