from app.database.database import Base, engine

# Importar modelos para que SQLAlchemy los registre
import app.models

def init_db():
    Base.metadata.create_all(bind=engine)