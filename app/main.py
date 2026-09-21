from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database.init_db import init_db

from app.routers.project_router import router as project_router
from app.routers.skill_router import router as skill_router
from app.routers import profile_router, social_link_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API for portfolio profile, social links, and skills.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.on_event("startup")
def create_database_tables() -> None:
    init_db()

app.include_router(project_router)
app.include_router(skill_router)
app.include_router(profile_router.router)
app.include_router(social_link_router.router)


@app.get("/")
def root():
    return {
        "message": "Portafolio Backend API",
        "database": settings.DB_NAME
    }
