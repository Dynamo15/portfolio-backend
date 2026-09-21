from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.skill_repository import SkillRepository
from app.schemas.skill import (
    SkillCreate,
    SkillUpdate,
    SkillResponse,
    
)

router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
    responses={
        404: {"description": "Resource not found"}
    },
)

repository = SkillRepository()


@router.post(
    "/",
    response_model=SkillResponse,
    status_code=201,
    summary="Create a new skill",
    description="Creates a new technology for the portfolio.",
    responses={
        201: {"description": "Skill created successfully."},
        409: {"description": "A skill with this name already exists."},
        422: {"description": "Validation error."},
    },
)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    existing_skill = repository.get_by_name(db, skill.name)

    if existing_skill:
        raise HTTPException(
            status_code=409,
            detail="A skill with this name already exists."
        )

    return repository.create(db, skill)


@router.get(
    "/",
    response_model=list[SkillResponse],
    summary="List skills",
    description="Returns all skills ordered by display order.",
)
def get_skills(db: Session = Depends(get_db)):
    return repository.get_all(db)


@router.get(
    "/{skill_id}",
    response_model=SkillResponse,
    summary="Get a skill by ID",
    description="Returns a single skill by its identifier.",
    responses={
        404: {"description": "Skill not found."}
    },
)
def get_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = repository.get_by_id(db, skill_id)

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    return skill


@router.put(
    "/{skill_id}",
    response_model=SkillResponse,
    summary="Update a skill",
    description="Updates an existing technology.",
    responses={
        404: {"description": "Skill not found."},
        409: {"description": "A skill with this name already exists."},
    },
)
def update_skill(
    skill_id: int,
    skill: SkillUpdate,
    db: Session = Depends(get_db),
):
    current_skill = repository.get_by_id(db, skill_id)
    if not current_skill:
        raise HTTPException(status_code=404, detail="Skill not found.")

    existing_skill = repository.get_by_name(db, skill.name) if skill.name else None

    if existing_skill and existing_skill.id != skill_id:
        raise HTTPException(
            status_code=409,
            detail="A skill with this name already exists."
        )

    updated_skill = repository.update(db, skill_id, skill)

    return updated_skill


@router.delete(
    "/{skill_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    summary="Delete a skill",
    description="Deletes a technology from the portfolio.",
    responses={
        404: {"description": "Skill not found."}
    },
)
def delete_skill(skill_id: int, db: Session = Depends(get_db)) -> Response:
    deleted_skill = repository.delete(db, skill_id)

    if not deleted_skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

