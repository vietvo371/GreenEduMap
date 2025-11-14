"""Pydantic schemas for User API."""

from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    role: str  # citizen, school, admin

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    avatar_url: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Citizen Feedback Schemas
class FeedbackBase(BaseModel):
    ward_name: str
    message: str
    image_url: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    user_id: int

class FeedbackResponse(FeedbackBase):
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
