from datetime import datetime
from pydantic import AnyUrl, BaseModel, ConfigDict, Field


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
    
    url: AnyUrl = Field(
        description="URL or contact link"
    )
    
    display_order: int = Field(
        ge=1,
        description="Display order of the sopcial link."
        
    )
    
    is_active: bool = True



class SocialLinkCreate(SocialLinkBase):
    pass


class SocialLinkUpdate(SocialLinkBase):
    pass


class SocialLinkResponse(SocialLinkBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    