"""Pydantic schemas for AI Analysis API."""

from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# AI Analysis Schemas
class AIAnalysisBase(BaseModel):
    ward_name: str
    corr_env_edu: float
    corr_energy: float
    recommendation: str

class AIAnalysisCreate(AIAnalysisBase):
    pass

class AIAnalysisResponse(AIAnalysisBase):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

# Green Actions Schemas
class GreenActionBase(BaseModel):
    ward_name: str
    action: str
    impact_score: float

class GreenActionCreate(GreenActionBase):
    pass

class GreenActionResponse(GreenActionBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class AIInsightsResponse(BaseModel):
    ai_analysis: list[AIAnalysisResponse]
    green_actions: list[GreenActionResponse]
