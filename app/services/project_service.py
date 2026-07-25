from sqlalchemy.orm import Session

from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate


class ProjectService:

    def __init__(self):
        self.repository = ProjectRepository()

    def create_project(self, db: Session, project: ProjectCreate):
        return self.repository.create(db, project)