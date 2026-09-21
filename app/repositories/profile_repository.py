from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile import ProfileUpdate


class ProfileRepository:

    def get(self, db: Session):
        return db.query(Profile).first()

    def update(
        self,
        db: Session,
        profile: Profile,
        data: ProfileUpdate,
    ):
        for field, value in data.model_dump(exclude_unset=True, mode="json").items():
            setattr(profile, field, value)

        db.commit()
        db.refresh(profile)

        return profile
