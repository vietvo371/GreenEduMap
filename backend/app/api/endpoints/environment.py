from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import AirQuality, WeatherData, EnergyData
from app.schemas.air_quality import AirQualityResponse, WeatherDataResponse, EnergyDataResponse

router = APIRouter(prefix="/api", tags=["environment"])

@router.get("/air-quality", response_model=list[AirQualityResponse])
def get_air_quality(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AirQuality).offset(skip).limit(limit).all()

@router.get("/weather", response_model=list[WeatherDataResponse])
def get_weather(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(WeatherData).offset(skip).limit(limit).all()

@router.get("/energy", response_model=list[EnergyDataResponse])
def get_energy(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(EnergyData).offset(skip).limit(limit).all()
