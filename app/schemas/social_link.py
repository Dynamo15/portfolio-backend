from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class SocialLinkBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
        description="Name of the social network."
    )
    
    icon: str = Field(
        min_length=1,
        max_length=100,
        description="Icon identifier used by the frontend."
    )
    
    url: HttpUrl = Field(
        description="URL or contact link"
    )
    
    display_order: int = Field(
        ge=1,
        description="Display order of the sopcial link."
        
    )
    
    is_active: bool = True



class SocialLinkCreate(SocialLinkBase):
    pass


class SocialLinkUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100, strip_whitespace=True)
    icon: str | None = Field(default=None, min_length=1, max_length=100, strip_whitespace=True)
    url: HttpUrl | None = None
    display_order: int | None = Field(default=None, ge=0)
    is_active: bool | None = None


class SocialLinkResponse(SocialLinkBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
