from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from app.db.models.user import User
from app.core.security import hash_password


def create_user(db: Session, email: str, password: str) -> User:
    # Business rule placeholder (future):
    # - password breach checks
    # - rate limiting
    # - domain restrictions

    hashed_pw = hash_password(password)

    user = User(
        email=email,
        hashed_password=hashed_pw
    )

    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    db.refresh(user)
    return user
