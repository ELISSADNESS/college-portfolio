from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends)

from ..config.db import get_db
# from ..models import Types as TypesModel
# from ..models import Works as WorksModel
from ..models import Authors as AuthorsModel
# from ..models import Works_Types as Works_TypesModel

from ..schemas import BaseAuthor, Author

from sqlalchemy.orm import Session

from typing import List

router = APIRouter(
    prefix="/app/authors",
    tags=["authors"]
)

@router.get("/", response_description="List all authors", response_model=List[Author], status_code=status.HTTP_200_OK)
def get_all_authors(db: Session=Depends(get_db)):
    authors = db.query(AuthorsModel).all()

    if authors == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothing found"
        )
    return authors

@router.post("/", response_description="Create new author", response_model=Author, status_code=status.HTTP_201_CREATED)
def create_author(author: BaseAuthor, db: Session=Depends(get_db)):
    new_author = AuthorsModel(
        name = author.name,
        login = author.login,
        password = author.password,
        email = author.email,
        photo = author.photo
    )

    db.add(new_author)

    db.commit()

    db.refresh(new_author)

    return new_author