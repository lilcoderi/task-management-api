from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional
from enum import Enum

class PriorityEnum(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str]
    category: str
    priority: PriorityEnum
    deadline: date

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    created_at: datetime 
    updated_at: datetime   

    class Config:
        orm_mode = True
