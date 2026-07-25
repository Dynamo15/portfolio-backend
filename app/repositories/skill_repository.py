from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate


class SkillRepository:

    def create(self, db: Session, skill: SkillCreate):
        db_skill = Skill(**skill.model_dump())

        db.add(db_skill)
        db.commit()
        db.refresh(db_skill)

        return db_skill

    def get_all(self, db: Session):
        return (
            db.query(Skill)
            .order_by(Skill.display_order)
            .all()
        )

    def get_by_id(self, db: Session, skill_id: int):
        return (
            db.query(Skill)
            .filter(Skill.id == skill_id)
            .first()
        )
        
    def get_by_name(self, db: Session, name: str):
        return (
            db.query(Skill)
            .filter(Skill.name == name)
            .first()
        )

    def update(
        self,
        db: Session,
        skill_id: int,
        skill: SkillUpdate
    ):
        db_skill = self.get_by_id(db, skill_id)

        if not db_skill:
            return None

        for key, value in skill.model_dump().items():
            setattr(db_skill, key, value)

        db.commit()
        db.refresh(db_skill)

        return db_skill

    def delete(self, db: Session, skill_id: int):
        db_skill = self.get_by_id(db, skill_id)

        if not db_skill:
            return None

        db.delete(db_skill)
        db.commit()

        return db_skill
    
    