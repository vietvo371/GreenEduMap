"""Database models module."""

from app.models.air_quality import AirQuality
from app.models.education import School, EducationQuality
from app.models.user import User
from app.models.ai_result import AIAnalysis

__all__ = [
    "AirQuality",
    "School",
    "EducationQuality",
    "User",
    "AIAnalysis",
]
