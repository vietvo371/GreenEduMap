"""Pydantic schemas for Air Quality API."""

from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Air Quality Schemas
class AirQualityBase(BaseModel):
    ward_name: str
    lat: float
    lng: float
    aqi: float
    pm25: float
    pm10: float
    no2: float
    so2: float
    co: float

class AirQualityCreate(AirQualityBase):
    pass

class AirQualityResponse(AirQualityBase):
    id: int
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Weather Data Schemas
class WeatherDataBase(BaseModel):
    ward_name: str
    lat: float
    lng: float
    temperature: float
    humidity: float
    wind_speed: float

class WeatherDataResponse(WeatherDataBase):
    id: int
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Energy Data Schemas
class EnergyDataBase(BaseModel):
    ward_name: str
    lat: float
    lng: float
    solar_potential_kw: float
    current_usage_kw: float

class EnergyDataResponse(EnergyDataBase):
    id: int
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Combined response
class EnvironmentDataResponse(BaseModel):
    air_quality: list[AirQualityResponse]
    weather_data: list[WeatherDataResponse]
    energy_data: list[EnergyDataResponse]
