from datetime import datetime

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

TextField = Annotated[str, Field(min_length=1, max_length=2_000, strip_whitespace=True)]


class ProfileBase(BaseModel):
    # Hero
    greeting_es: TextField
    greeting_en: TextField

    full_name: Annotated[str, Field(min_length=1, max_length=150, strip_whitespace=True)]

    profession_es: Annotated[str, Field(min_length=1, max_length=150, strip_whitespace=True)]
    profession_en: Annotated[str, Field(min_length=1, max_length=150, strip_whitespace=True)]

    phrase_es: TextField
    phrase_en: TextField

    # About
    about_title_es: TextField
    about_title_en: TextField

    about_description_es: TextField
    about_description_en: TextField

    status_es: TextField
    status_en: TextField

    work_mode_es: TextField
    work_mode_en: TextField

    location_es: str = Field(max_length=100, default="")
    location_en: str = Field(max_length=100, default="")

    # Resume
    resume_filename: str | None = Field(default=None, max_length=255)
    resume_url: HttpUrl | None = None


class ProfileUpdate(BaseModel):
    greeting_es: TextField | None = None
    greeting_en: TextField | None = None
    full_name: Annotated[str, Field(min_length=1, max_length=150, strip_whitespace=True)] | None = None
    profession_es: Annotated[str, Field(min_length=1, max_length=150, strip_whitespace=True)] | None = None
    profession_en: Annotated[str, Field(min_length=1, max_length=150, strip_whitespace=True)] | None = None
    phrase_es: TextField | None = None
    phrase_en: TextField | None = None
    about_title_es: TextField | None = None
    about_title_en: TextField | None = None
    about_description_es: TextField | None = None
    about_description_en: TextField | None = None
    status_es: TextField | None = None
    status_en: TextField | None = None
    work_mode_es: TextField | None = None
    work_mode_en: TextField | None = None
    location_es: str | None = Field(default=None, max_length=100)
    location_en: str | None = Field(default=None, max_length=100)
    resume_filename: str | None = Field(default=None, max_length=255)
    resume_url: HttpUrl | None = None


class ProfileResponse(ProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
