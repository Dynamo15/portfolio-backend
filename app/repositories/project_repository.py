from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


class ProjectRepository:
    
    def create(self, db: Session, project: ProjectCreate) -> Project:
        
        db_project = Project(
            title=project.title,
            slug=project.slug,
            short_description=project.short_description,
            description=project.description,
            github_url=str(project.demo_url) if project.github_url else None,
            demo_url=str(project.demo_url) if project.demo_url else None,
            image_url=project.image_url,
            featured=project.featured,
            active=project.active,
            )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        
        return db_project