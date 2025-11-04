"""Main API Router."""

from fastapi import APIRouter
from app.api.endpoints import air_quality, ai_analysis

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(air_quality.router)
api_router.include_router(ai_analysis.router)
