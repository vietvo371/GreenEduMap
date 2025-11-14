"""Air Quality model for storing environmental data."""

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db import Base


class AirQuality(Base):
    """Air Quality Data Model"""
    __tablename__ = "air_quality"

    id = Column(Integer, primary_key=True, index=True)
    ward_name = Column(String, index=True)
    lat = Column(Float)
    lng = Column(Float)
    aqi = Column(Float)
    pm25 = Column(Float)
    pm10 = Column(Float)
    no2 = Column(Float)
    so2 = Column(Float)
    co = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class WeatherData(Base):
    """Weather Data Model"""
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    ward_name = Column(String, index=True)
    lat = Column(Float)
    lng = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class EnergyData(Base):
    """Energy Data Model"""
    __tablename__ = "energy_data"

    id = Column(Integer, primary_key=True, index=True)
    ward_name = Column(String, index=True)
    lat = Column(Float)
    lng = Column(Float)
    solar_potential_kw = Column(Float)
    current_usage_kw = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
