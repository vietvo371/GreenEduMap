from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import AIAnalysis, GreenAction
from app.schemas.ai_result import AIAnalysisResponse, GreenActionResponse, AIAnalysisCreate, GreenActionCreate

router = APIRouter(prefix="/api", tags=["ai"])

@router.get("/ai/analysis", response_model=list[AIAnalysisResponse])
def list_ai_analysis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(AIAnalysis).offset(skip).limit(limit).all()

@router.post("/ai/analysis", response_model=AIAnalysisResponse)
def create_ai_analysis(analysis: AIAnalysisCreate, db: Session = Depends(get_db)):
    db_analysis = AIAnalysis(**analysis.dict())
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

@router.get("/ai/recommendations", response_model=list[GreenActionResponse])
def list_green_actions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(GreenAction).offset(skip).limit(limit).all()

@router.post("/ai/recommendations", response_model=GreenActionResponse)
def create_green_action(action: GreenActionCreate, db: Session = Depends(get_db)):
    db_action = GreenAction(**action.dict())
    db.add(db_action)
    db.commit()
    db.refresh(db_action)
    return db_action
