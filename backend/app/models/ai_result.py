"""AI analysis results model."""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Text
from datetime import datetime
from app.db.base import Base


class AIAnalysis(Base):
    """AI Analysis results model."""

    __tablename__ = "ai_analysis"

    id = Column(Integer, primary_key=True, index=True)

    # Analysis metadata
    analysis_type = Column(String(100), nullable=False)  # correlation, prediction, clustering
    title = Column(String(255))
    description = Column(Text)

    # Input data
    input_parameters = Column(JSON, nullable=False)

    # Results
    correlation_coefficient = Column(Float, nullable=True)
    model_accuracy = Column(Float, nullable=True)
    predictions = Column(JSON, nullable=True)
    insights = Column(JSON, nullable=True)

    # Recommendation
    recommendation = Column(Text)
    recommendation_priority = Column(String(50))  # high, medium, low

    # Model info
    model_name = Column(String(100))
    model_version = Column(String(50))

    # Status
    status = Column(String(50), default="completed")  # processing, completed, failed
    error_message = Column(Text, nullable=True)

    # Dates
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Metadata
    metadata = Column(JSON, nullable=True)
