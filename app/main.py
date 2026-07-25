from fastapi import FastAPI
from app.core.config import settings
from app.database.init_db import init_db
from app.routers.project_router import router as project_router
from app.routers.skill_router import router as skill_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

init_db()
app.include_router(project_router)
app.include_router(skill_router)

@app.get("/")
def root():
    return {
        "message": "Portafolio Backend API",
        "database": settings.DB_NAME
    }