"""Database models module."""

from app.models.air_quality import AirQuality, WeatherData, EnergyData
from app.models.education import School, Course
from app.models.user import User, CitizenFeedback
from app.models.ai_result import AIAnalysis, GreenAction

__all__ = [
    "AirQuality",
    "WeatherData",
    "EnergyData",
    "School",
    "Course",
    "User",
    "CitizenFeedback",
    "AIAnalysis",
    "GreenAction",
]
