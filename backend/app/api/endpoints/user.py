from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import User, CitizenFeedback
from app.schemas.user import UserResponse, FeedbackResponse, UserCreate, FeedbackCreate

router = APIRouter(prefix="/api", tags=["users"])

@router.get("/users", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    import bcrypt
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
    db_user = User(full_name=user.full_name, email=user.email, role=user.role, password_hash=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/feedback", response_model=list[FeedbackResponse])
def list_feedback(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(CitizenFeedback).offset(skip).limit(limit).all()

@router.post("/feedback", response_model=FeedbackResponse)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = CitizenFeedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback
