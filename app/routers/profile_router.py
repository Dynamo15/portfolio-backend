from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.profile_repository import ProfileRepository
from app.schemas.profile import ProfileResponse, ProfileUpdate


router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)

repository = ProfileRepository()


@router.get(
    "/",
    response_model=ProfileResponse,
    summary="Get profile",
    description="Returns the portfolio profile information.",
    responses={
        404: {"description": "Profile not found."},
    },
)
def get_profile(db: Session = Depends(get_db)):
    profile = repository.get(db)

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found.",
        )

    return profile


@router.put(
    "/",
    response_model=ProfileResponse,
    summary="Update profile",
    description="Updates the portfolio profile information.",
    responses={
        404: {"description": "Profile not found."},
    },
)
def update_profile(
    profile_data: ProfileUpdate,
    db: Session = Depends(get_db),
):
    profile = repository.get(db)

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found.",
        )

    return repository.update(
        db,
        profile,
        profile_data,
    )