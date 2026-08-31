from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field



class SkillBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
        description="Technology name."
    )

    icon: str = Field(
        min_length=2,
        max_length=100,
        description="Technology icon identifier."
    )

    display_order: int = Field(
        gt=0,
        description="Display order."
    )

class SkillCreate(SkillBase):
    pass


class SkillUpdate(SkillBase):
    pass


class SkillResponse(SkillBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)