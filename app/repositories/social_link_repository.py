from sqlalchemy.orm import Session

from app.models.social_link import SocialLink
from app.schemas.social_link import SocialLinkCreate, SocialLinkUpdate


class SocialLinkRepository:

    def get_all(self, db: Session):
        return (
            db.query(SocialLink)
            .order_by(SocialLink.display_order)
            .all()
        )

    def get_by_id(self, db: Session, social_link_id: int):
        return db.query(SocialLink).filter(
            SocialLink.id == social_link_id
        ).first()

    def create(self, db: Session, social_link: SocialLinkCreate):
        db_social_link = SocialLink(
            **social_link.model_dump()
        )

        db.add(db_social_link)
        db.commit()
        db.refresh(db_social_link)

        return db_social_link

    def update(
        self,
        db: Session,
        social_link_id: int,
        social_link: SocialLinkUpdate,
    ):
        db_social_link = self.get_by_id(db, social_link_id)

        if not db_social_link:
            return None

        for field, value in social_link.model_dump().items():
            setattr(db_social_link, field, value)

        db.commit()
        db.refresh(db_social_link)

        return db_social_link

    def delete(self, db: Session, social_link_id: int):
        db_social_link = self.get_by_id(db, social_link_id)

        if not db_social_link:
            return None

        db.delete(db_social_link)
        db.commit()

        return db_social_link