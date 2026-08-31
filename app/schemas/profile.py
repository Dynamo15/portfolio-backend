from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    # Hero
    greeting_es: str
    greeting_en: str

    full_name: str

    profession_es: str
    profession_en: str

    phrase_es: str
    phrase_en: str

    # About
    about_title_es: str
    about_title_en: str

    about_description_es: str
    about_description_en: str

    status_es: str
    status_en: str

    work_mode_es: str
    work_mode_en: str

    location_es: str
    location_en: str

    # Resume
    resume_filename: str | None = None
    resume_url: str | None = None


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)