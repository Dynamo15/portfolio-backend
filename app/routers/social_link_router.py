from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.social_link_repository import SocialLinkRepository
from app.schemas.social_link import (
    SocialLinkCreate,
    SocialLinkUpdate,
    SocialLinkResponse
)


router = APIRouter(
    prefix="/social-links",
    tags=["Social Links"],
    responses={404: {"description": "Social link not found."}},
)

repository = SocialLinkRepository()


@router.get(
    "/",
    response_model=list[SocialLinkResponse],
    summary="Get social links",
    description="Returns all social links ordered by display order."
)
def get_social_links(
    db: Session = Depends(get_db)
):
    return repository.get_all(db)


@router.get(
    "/{social_link_id}",
    response_model=SocialLinkResponse,
    summary="Get social link",
    description="Returns a social link by ID."
)
def get_social_link(
    social_link_id: int,
    db: Session = Depends(get_db)
):
    social_link = repository.get_by_id(db, social_link_id)

    if not social_link:
        raise HTTPException(
            status_code=404,
            detail="Social link not found"
        )

    return social_link


@router.post(
    "/",
    response_model=SocialLinkResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create social link",
    description="Creates a new social link."
)
def create_social_link(
    social_link: SocialLinkCreate,
    db: Session = Depends(get_db)
):
    return repository.create(db, social_link)


@router.put(
    "/{social_link_id}",
    response_model=SocialLinkResponse,
    summary="Update social link",
    description="Updates an existing social link."
)
def update_social_link(
    social_link_id: int,
    social_link: SocialLinkUpdate,
    db: Session = Depends(get_db)
):
    updated_social_link = repository.update(
        db,
        social_link_id,
        social_link
    )

    if not updated_social_link:
        raise HTTPException(
            status_code=404,
            detail="Social link not found"
        )

    return updated_social_link


@router.delete(
    "/{social_link_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    summary="Delete social link",
    description="Deletes a social link."
)
def delete_social_link(
    social_link_id: int,
    db: Session = Depends(get_db)
) -> Response:
    deleted_social_link = repository.delete(
        db,
        social_link_id
    )

    if not deleted_social_link:
        raise HTTPException(
            status_code=404,
            detail="Social link not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
