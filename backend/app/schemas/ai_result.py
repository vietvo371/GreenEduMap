"""Pydantic schemas for AI Analysis API."""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any, Dict


class AIAnalysisBase(BaseModel):
    """Base AI analysis schema."""

    analysis_type: str
    title: Optional[str] = None
    description: Optional[str] = None


class CorrelationAnalysisRequest(AIAnalysisBase):
    """Schema for correlation analysis request."""

    env_values: list[float]
    edu_scores: list[float]


class CorrelationAnalysisResponse(BaseModel):
    """Schema for correlation analysis response."""

    correlation_coefficient: float
    p_value: Optional[float] = None
    slope: float
    intercept: float
    r_squared: float
    interpretation: str
    recommendation: str


class PredictionRequest(AIAnalysisBase):
    """Schema for prediction request."""

    features: Dict[str, Any]
    model_name: Optional[str] = None


class PredictionResponse(BaseModel):
    """Schema for prediction response."""

    predicted_value: float
    confidence: float
    model_version: str
    explanation: str


class AIAnalysisResultResponse(BaseModel):
    """Schema for stored AI analysis result."""

    id: int
    analysis_type: str
    title: Optional[str]
    correlation_coefficient: Optional[float]
    model_accuracy: Optional[float]
    predictions: Optional[Dict[str, Any]]
    insights: Optional[Dict[str, Any]]
    recommendation: Optional[str]
    recommendation_priority: Optional[str]
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AIAnalysisListResponse(BaseModel):
    """Schema for AI analysis list response."""

    total: int
    items: list[AIAnalysisResultResponse]
