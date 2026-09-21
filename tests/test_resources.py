import unittest

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.database import Base
from app.database.init_db import INITIAL_PROFILE
from app.models import Profile
from app.repositories.profile_repository import ProfileRepository
from app.repositories.skill_repository import SkillRepository
from app.repositories.social_link_repository import SocialLinkRepository
from app.routers.skill_router import create_skill
from app.schemas.profile import ProfileUpdate
from app.schemas.skill import SkillCreate, SkillUpdate
from app.schemas.social_link import SocialLinkCreate, SocialLinkUpdate


class ResourceRepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.engine = create_engine("sqlite+pysqlite:///:memory:")
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.engine.dispose()

    def setUp(self) -> None:
        self.db = self.Session()
        for table in reversed(Base.metadata.sorted_tables):
            self.db.execute(table.delete())
        self.db.add(Profile(**INITIAL_PROFILE))
        self.db.commit()

    def tearDown(self) -> None:
        self.db.close()

    def test_profile_get_and_partial_update(self) -> None:
        repository = ProfileRepository()
        profile = repository.get(self.db)

        updated = repository.update(
            self.db, profile, ProfileUpdate(full_name="Ada Lovelace")
        )

        self.assertEqual(updated.full_name, "Ada Lovelace")
        self.assertEqual(updated.greeting_es, INITIAL_PROFILE["greeting_es"])

    def test_skill_crud_and_duplicate_conflict(self) -> None:
        repository = SkillRepository()
        skill = repository.create(
            self.db, SkillCreate(name="Python", icon="python", display_order=1)
        )

        self.assertEqual(repository.get_all(self.db), [skill])
        self.assertEqual(
            repository.update(self.db, skill.id, SkillUpdate(icon="python-logo")).icon,
            "python-logo",
        )

        with self.assertRaises(HTTPException) as error:
            create_skill(
                SkillCreate(name="Python", icon="python", display_order=2), self.db
            )
        self.assertEqual(error.exception.status_code, 409)

        self.assertIsNotNone(repository.delete(self.db, skill.id))
        self.assertIsNone(repository.get_by_id(self.db, skill.id))

    def test_social_link_crud_and_ordering(self) -> None:
        repository = SocialLinkRepository()
        github = repository.create(
            self.db,
            SocialLinkCreate(
                name="GitHub",
                icon="github",
                url="https://github.com/example",
                display_order=2,
            ),
        )
        linkedin = repository.create(
            self.db,
            SocialLinkCreate(
                name="LinkedIn",
                icon="linkedin",
                url="https://linkedin.com/in/example",
                display_order=1,
            ),
        )

        self.assertEqual(
            [link.id for link in repository.get_all(self.db)], [linkedin.id, github.id]
        )
        self.assertFalse(
            repository.update(self.db, github.id, SocialLinkUpdate(is_active=False)).is_active
        )
        self.assertIsNotNone(repository.delete(self.db, github.id))


if __name__ == "__main__":
    unittest.main()
