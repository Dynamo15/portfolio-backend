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
    __tablename__= "projects"
    
    id = Integer
    

class Project(Base):
    __tablename__="projects"
    