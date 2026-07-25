from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text
)
from sqlalchemy.sql import func

from app.database.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    slug = Column(String(250), unique=True, nullable=False)

    short_description = Column(String(300))

    full_description = Column(Text)

    cover_image = Column(String(500))

    github_url = Column(String(500))

    live_demo_url = Column(String(500))

    documentation_url = Column(String(500))

    status = Column(String(50), default="In Development")

    featured = Column(Boolean, default=False)

    published = Column(Boolean, default=True)

    display_order = Column(Integer, default=0)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )