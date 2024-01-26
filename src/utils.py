import jwt
from sqlalchemy.orm import Session

from src.db import engine


def generate_token(username: str, secret_key: str) -> str:
    payload = {"username": username}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token


def get_db():
    with Session(engine) as session:
        yield session
