"""Air Quality API endpoints."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.air_quality import AirQuality
from app.schemas.air_quality import (
    AirQualityCreate,
    AirQualityResponse,
    AirQualityListResponse,
    AQIAlert,
)
from app.services.open_data_service import OpenDataService

router = APIRouter(prefix="/air-quality", tags=["Air Quality"])


@router.get("/", response_model=AirQualityListResponse)
async def list_air_quality(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    city: str = Query("Hanoi", min_length=1),
    db: Session = Depends(get_db)
):
    """Get air quality records."""
    query = db.query(AirQuality).filter(AirQuality.city == city)
    total = query.count()
    items = query.offset(skip).limit(limit).all()

    return AirQualityListResponse(
        total=total,
        items=[AirQualityResponse.from_orm(item) for item in items]
    )


@router.get("/{air_quality_id}", response_model=AirQualityResponse)
async def get_air_quality(
    air_quality_id: int,
    db: Session = Depends(get_db)
):
    """Get specific air quality record."""
    db_air_quality = db.query(AirQuality).filter(
        AirQuality.id == air_quality_id
    ).first()

    if not db_air_quality:
        raise HTTPException(status_code=404, detail="Air quality record not found")

    return AirQualityResponse.from_orm(db_air_quality)


@router.post("/", response_model=AirQualityResponse)
async def create_air_quality(
    air_quality: AirQualityCreate,
    db: Session = Depends(get_db)
):
    """Create new air quality record."""
    db_air_quality = AirQuality(**air_quality.dict())
    db.add(db_air_quality)
    db.commit()
    db.refresh(db_air_quality)

    return AirQualityResponse.from_orm(db_air_quality)


@router.get("/fetch/openaq")
async def fetch_from_openaq(city: str = Query("Hanoi", min_length=1)):
    """Fetch air quality data from OpenAQ API."""
    data = await OpenDataService.fetch_openaq_data(city)
    return data


@router.get("/alerts/high")
async def get_aqi_alerts(
    threshold: float = Query(150.0, ge=0),
    db: Session = Depends(get_db)
) -> list[AQIAlert]:
    """Get air quality alerts where AQI exceeds threshold."""
    high_aqi_records = db.query(AirQuality).filter(
        AirQuality.aqi >= threshold
    ).all()

    alerts = []
    for record in high_aqi_records:
        # Determine AQI level
        if record.aqi <= 50:
            aqi_level = "Good"
        elif record.aqi <= 100:
            aqi_level = "Moderate"
        elif record.aqi <= 150:
            aqi_level = "Unhealthy for Sensitive Groups"
        elif record.aqi <= 200:
            aqi_level = "Unhealthy"
        else:
            aqi_level = "Very Unhealthy"

        # Determine main pollutant
        pollutants = {
            "PM2.5": record.pm25 or 0,
            "PM10": record.pm10 or 0,
            "NO2": record.no2 or 0,
            "O3": record.o3 or 0,
        }
        main_pollutant = max(pollutants, key=pollutants.get)

        alerts.append(AQIAlert(
            location=record.ward_name,
            aqi_level=aqi_level,
            aqi_value=record.aqi,
            main_pollutant=main_pollutant,
            recommendation="Hạn chế hoạt động ngoài trời, sử dụng khẩu trang N95"
        ))

    return alerts
