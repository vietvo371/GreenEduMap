from pydantic import BaseModel, ConfigDict
from datetime import datetime, date
from typing import Optional

# School Schemas
class SchoolBase(BaseModel):
    school_name: str
    ward_name: str
    lat: float
    lng: float
    green_programs_count: int = 0
    avg_score: Optional[float] = None
    energy_saving_kw: Optional[float] = None

class SchoolCreate(SchoolBase):
    pass

class SchoolResponse(SchoolBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Course Schemas
class CourseBase(BaseModel):
    school_id: int
    title: str
    description: str
    type: str
    students: int
    start_date: date
    end_date: date

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class SchoolDetailResponse(SchoolResponse):
    courses: list[CourseResponse] = []
