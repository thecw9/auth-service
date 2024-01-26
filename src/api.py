from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.db.model import User
from src.utils import get_db

router = APIRouter()


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.username == form_data.username).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # check password
    if not db_user.password == form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # check is_active
    if not db_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # get token
    access_token = db_user.access_token

    # return token
    return {"code": 200, "message": "success", "data": {"token": access_token}}


class Token(BaseModel):
    access_token: str


# test token
@router.post("/verify_token")
async def verify_token(token: Token, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.access_token == token.access_token).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    is_superuser = db_user.is_superuser
    return {"code": 200, "message": "success", "data": {"is_superuser": is_superuser}}
