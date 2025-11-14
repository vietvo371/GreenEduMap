from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import School, Course
from app.schemas.education import SchoolResponse, CourseResponse, SchoolCreate, CourseCreate

router = APIRouter(prefix="/api", tags=["education"])

@router.get("/schools", response_model=list[SchoolResponse])
def list_schools(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(School).offset(skip).limit(limit).all()

@router.post("/schools", response_model=SchoolResponse)
def create_school(school: SchoolCreate, db: Session = Depends(get_db)):
    db_school = School(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

@router.get("/courses", response_model=list[CourseResponse])
def list_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Course).offset(skip).limit(limit).all()

@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
