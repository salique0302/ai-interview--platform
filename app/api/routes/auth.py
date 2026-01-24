from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserPublic
from app.services.user_service import create_user
from app.db.deps import get_db

router = APIRouter()


@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.email, user.password)
