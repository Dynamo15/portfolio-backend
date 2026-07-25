from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime


class ProjectBase(BaseModel):
    title: str
    slug: str
    short_description: str
    description: str

    description: Optional[str] = None

    github_url: Optional[HttpUrl] = None
    demo_url: Optional[HttpUrl] = None

    image_url: Optional[str] = None

    featured: bool = False

    active: bool = True
    
class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime
    update_at: datetime

    class Config:
        from_attributes = True