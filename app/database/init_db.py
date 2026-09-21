from sqlalchemy.orm import Session

from app.database.database import Base, SessionLocal, engine

# Importar modelos para que SQLAlchemy los registre
from app.models import Profile


INITIAL_PROFILE = {
    "id": 1,
    "greeting_es": "Hola, soy",
    "greeting_en": "Hello, I am",
    "full_name": "Portfolio Owner",
    "profession_es": "Desarrollador de software",
    "profession_en": "Software developer",
    "phrase_es": "Construyo experiencias digitales claras y útiles.",
    "phrase_en": "I build clear and useful digital experiences.",
    "about_title_es": "Sobre mí",
    "about_title_en": "About me",
    "about_description_es": "Actualiza esta información desde el panel administrativo.",
    "about_description_en": "Update this information from the administrative panel.",
    "status_es": "Disponible para colaborar",
    "status_en": "Available to collaborate",
    "work_mode_es": "Remoto",
    "work_mode_en": "Remote",
    "location_es": "",
    "location_en": "",
}


def _create_initial_profile(db: Session) -> None:
    if db.get(Profile, 1) is None:
        db.add(Profile(**INITIAL_PROFILE))
        db.commit()

def init_db():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        _create_initial_profile(db)
