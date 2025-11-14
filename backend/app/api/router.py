"""Main API Router."""

from fastapi import APIRouter
from app.api.endpoints import environment, education, user, ai

api_router = APIRouter()
api_router.include_router(environment.router)
api_router.include_router(education.router)
api_router.include_router(user.router)
api_router.include_router(ai.router)
