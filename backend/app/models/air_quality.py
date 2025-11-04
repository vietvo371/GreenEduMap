"""Air Quality model for storing air quality measurements."""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from datetime import datetime
from app.db.base import Base


class AirQuality(Base):
    """Air Quality monitoring data model."""

    __tablename__ = "air_quality"

    id = Column(Integer, primary_key=True, index=True)

    # Location information
    ward_name = Column(String(255), nullable=False)
    district = Column(String(255))
    city = Column(String(255), default="Hanoi")
    latitude = Column(Float)
    longitude = Column(Float)

    # Air quality measurements
    aqi = Column(Float, nullable=False)  # Air Quality Index
    pm25 = Column(Float)  # PM2.5
    pm10 = Column(Float)  # PM10
    no2 = Column(Float)   # Nitrogen Dioxide
    o3 = Column(Float)    # Ozone
    so2 = Column(Float)   # Sulfur Dioxide
    co = Column(Float)    # Carbon Monoxide

    # Additional data
    data_source = Column(String(100), default="OpenAQ")
    measurement_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Metadata
    metadata = Column(JSON, nullable=True)
