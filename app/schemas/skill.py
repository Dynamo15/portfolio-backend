from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field



class SkillBase(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100,
        description="Technology name."
    )

    icon: str = Field(
        min_length=1,
        max_length=100,
        description="Technology icon identifier."
    )

    display_order: int = Field(
        ge=0,
        description="Display order."
    )

class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100, strip_whitespace=True)
    icon: str | None = Field(default=None, min_length=1, max_length=100, strip_whitespace=True)
    display_order: int | None = Field(default=None, ge=0)


class SkillResponse(SkillBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
