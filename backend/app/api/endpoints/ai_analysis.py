"""AI Analysis API endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.models.ai_result import AIAnalysis
from app.schemas.ai_result import (
    CorrelationAnalysisRequest,
    CorrelationAnalysisResponse,
    AIAnalysisResultResponse,
    AIAnalysisListResponse,
)
from app.services.ai_service import AIService

router = APIRouter(prefix="/ai", tags=["AI Analysis"])


@router.post("/analyze/correlation", response_model=CorrelationAnalysisResponse)
async def analyze_correlation(
    request: CorrelationAnalysisRequest
):
    """Analyze correlation between environmental and educational data."""
    try:
        if len(request.env_values) != len(request.edu_scores):
            raise HTTPException(
                status_code=400,
                detail="env_values and edu_scores must have equal length"
            )

        if len(request.env_values) < 2:
            raise HTTPException(
                status_code=400,
                detail="At least 2 data points required"
            )

        import numpy as np
        from scipy.stats import pearsonr
        from sklearn.linear_model import LinearRegression

        # Prepare data
        X = np.array(request.env_values).reshape(-1, 1)
        y = np.array(request.edu_scores)

        # Linear regression
        model = LinearRegression().fit(X, y)

        # Correlation
        corr, p_value = pearsonr(request.env_values, request.edu_scores)

        # R-squared
        r_squared = model.score(X, y)

        # Interpretation
        if abs(corr) < 0.3:
            interpretation = "Mối tương quan yếu"
        elif abs(corr) < 0.7:
            interpretation = "Mối tương quan vừa phải"
        else:
            interpretation = "Mối tương quan mạnh"

        # Recommendation
        if corr < -0.5:
            recommendation = "Môi trường tốt nhưng giáo dục yếu - cần tăng cường giáo dục"
        elif corr > 0.5:
            recommendation = "Cả môi trường lẫn giáo dục đều tốt - duy trì xu hướng này"
        else:
            recommendation = "Không có mối tương quan rõ ràng - cần khảo sát thêm"

        return CorrelationAnalysisResponse(
            correlation_coefficient=float(corr),
            p_value=float(p_value),
            slope=float(model.coef_[0]),
            intercept=float(model.intercept_),
            r_squared=float(r_squared),
            interpretation=interpretation,
            recommendation=recommendation
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze/ward")
async def analyze_ward(
    ward_name: str,
    air_quality_data: list = None,
    school_data: list = None,
    energy_data: list = None,
):
    """Analyze a specific ward's environmental-educational data."""
    try:
        results = AIService.analyze_correlation(
            air_quality_data or [],
            school_data or [],
            energy_data or [],
            ward_name
        )

        return {
            "success": True,
            "data": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/cluster/wards")
async def cluster_wards(wards_data: list):
    """Cluster wards based on environmental and educational metrics."""
    try:
        results = AIService.cluster_wards(wards_data)
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/predict/impact")
async def predict_action_impact(
    action: str,
    current_aqi: int = 100,
    current_energy: float = 50.0
):
    """Predict impact of green actions."""
    try:
        impact = AIService.predict_impact(action, current_aqi, current_energy)

        return {
            "action": action,
            "current_metrics": {
                "aqi": current_aqi,
                "energy_percentage": current_energy
            },
            "predicted_impact": impact
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/results", response_model=AIAnalysisListResponse)
async def list_analysis_results(
    skip: int = 0,
    limit: int = 10,
    analysis_type: str = None,
    db: Session = Depends(get_db)
):
    """List AI analysis results."""
    query = db.query(AIAnalysis)

    if analysis_type:
        query = query.filter(AIAnalysis.analysis_type == analysis_type)

    total = query.count()
    items = query.offset(skip).limit(limit).all()

    return AIAnalysisListResponse(
        total=total,
        items=[AIAnalysisResultResponse.from_orm(item) for item in items]
    )


@router.get("/results/{result_id}", response_model=AIAnalysisResultResponse)
async def get_analysis_result(
    result_id: int,
    db: Session = Depends(get_db)
):
    """Get specific AI analysis result."""
    result = db.query(AIAnalysis).filter(
        AIAnalysis.id == result_id
    ).first()

    if not result:
        raise HTTPException(status_code=404, detail="Analysis result not found")

    return AIAnalysisResultResponse.from_orm(result)
