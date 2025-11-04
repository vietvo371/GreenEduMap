"""Education model for storing school and education data."""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from datetime import datetime
from app.db.base import Base


class School(Base):
    """School information model."""

    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False, index=True)
    code = Column(String(50), unique=True)

    # Location
    district = Column(String(255))
    ward = Column(String(255))
    city = Column(String(255), default="Hanoi")
    latitude = Column(Float)
    longitude = Column(Float)
    address = Column(String(500))

    # School info
    school_type = Column(String(100))  # Elementary, Middle, High, University
    education_level = Column(String(100))
    total_students = Column(Integer)

    # Contact
    phone = Column(String(20))
    email = Column(String(255))
    website = Column(String(500))

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(JSON, nullable=True)


class EducationQuality(Base):
    """Education quality metrics."""

    __tablename__ = "education_quality"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer, nullable=False, index=True)

    # Metrics
    exam_score = Column(Float)
    pass_rate = Column(Float)
    graduation_rate = Column(Float)
    student_satisfaction = Column(Float)  # 1-10

    # Environmental impact
    green_areas_m2 = Column(Float)
    energy_efficiency_rating = Column(String(50))  # A, B, C, D
    recycling_program = Column(String(255))

    academic_year = Column(String(20))  # "2023-2024"

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(JSON, nullable=True)
