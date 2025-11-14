"""AI analysis results model."""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.db import Base


class AIAnalysis(Base):
    """AI Analysis Model"""
    __tablename__ = "ai_analysis"

    id = Column(Integer, primary_key=True, index=True)
    ward_name = Column(String, index=True)
    corr_env_edu = Column(Float)  # Correlation between environment & education
    corr_energy = Column(Float)   # Correlation between energy & education
    recommendation = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class GreenAction(Base):
    """Green Actions Recommendation Model"""
    __tablename__ = "green_actions"

    id = Column(Integer, primary_key=True, index=True)
    ward_name = Column(String, index=True)
    action = Column(Text)  # Recommended green action
    impact_score = Column(Float)  # Expected impact (0-100)
    created_at = Column(DateTime, default=datetime.utcnow)

