from datetime import UTC, datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database.database import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    icon = Column(String(100), nullable=False)
    display_order = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )
