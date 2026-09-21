from datetime import UTC, datetime

from sqlalchemy import CheckConstraint, Column, DateTime, Integer, String, Text

from app.database.database import Base


class Profile(Base):
    __tablename__ = "profiles"
    __table_args__ = (CheckConstraint("id = 1", name="single_profile_id"),)

    id = Column(Integer, primary_key=True, default=1)

    # Hero
    greeting_es = Column(String(100), nullable=False)
    greeting_en = Column(String(100), nullable=False)

    full_name = Column(String(150), nullable=False)

    profession_es = Column(String(150), nullable=False)
    profession_en = Column(String(150), nullable=False)

    phrase_es = Column(Text, nullable=False)
    phrase_en = Column(Text, nullable=False)

    # About
    about_title_es = Column(String(100), nullable=False)
    about_title_en = Column(String(100), nullable=False)

    about_description_es = Column(Text, nullable=False)
    about_description_en = Column(Text, nullable=False)

    status_es = Column(String(100), nullable=False)
    status_en = Column(String(100), nullable=False)

    work_mode_es = Column(String(100), nullable=False)
    work_mode_en = Column(String(100), nullable=False)

    location_es = Column(String(100), nullable=False)
    location_en = Column(String(100), nullable=False)

    # Resume
    resume_filename = Column(String(255), nullable=True)
    resume_url = Column(String(255), nullable=True)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
