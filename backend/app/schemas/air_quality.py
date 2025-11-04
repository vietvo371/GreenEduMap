"""Pydantic schemas for Air Quality API."""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AirQualityBase(BaseModel):
    """Base schema for air quality."""

    ward_name: str
    district: Optional[str] = None
    city: Optional[str] = "Hanoi"
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    aqi: float
    pm25: Optional[float] = None
    pm10: Optional[float] = None
    no2: Optional[float] = None
    o3: Optional[float] = None
    so2: Optional[float] = None
    co: Optional[float] = None
    data_source: Optional[str] = "OpenAQ"


class AirQualityCreate(AirQualityBase):
    """Schema for creating air quality record."""
    pass


class AirQualityUpdate(BaseModel):
    """Schema for updating air quality record."""

    aqi: Optional[float] = None
    pm25: Optional[float] = None
    pm10: Optional[float] = None
    no2: Optional[float] = None
    o3: Optional[float] = None
    so2: Optional[float] = None
    co: Optional[float] = None


class AirQualityResponse(AirQualityBase):
    """Schema for air quality API response."""

    id: int
    measurement_date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AirQualityListResponse(BaseModel):
    """Schema for air quality list response."""

    total: int
    items: list[AirQualityResponse]


class AQIAlert(BaseModel):
    """Schema for AQI alert when pollution is high."""

    location: str
    aqi_level: str  # "Good", "Moderate", "Unhealthy for Sensitive Groups", etc.
    aqi_value: float
    main_pollutant: str
    recommendation: str
