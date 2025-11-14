"""Education model for storing school and education data."""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Date, Text
from datetime import datetime
from app.db import Base


class School(Base):
    """School Model"""
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String, index=True)
    ward_name = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    green_programs_count = Column(Integer, default=0)
    avg_score = Column(Float)
    energy_saving_kw = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Course(Base):
    """Course/Program Model"""
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, ForeignKey("schools.id"), index=True)
    title = Column(String)
    description = Column(Text)
    type = Column(String)  # Recycling, Solar, TreePlanting, etc.
    students = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
