from datetime import datetime

from sqlalchemy.orm import Session
from src.config import Config
from src.db import engine
from src.db.model import Base, User
from src.utils import generate_token

config = Config()


def init_db():
    # Create tables
    Base.metadata.create_all(engine)

    # check user is exist
    with Session(engine) as session:
        user = (
            session.query(User).filter(User.username == config.FIRST_SUPERUSER).first()
        )
        if user:
            return

    # Create a default user
    with Session(engine) as session:
        user = User(
            username=config.FIRST_SUPERUSER,
            email=config.FIRST_SUPERUSER_EMAIL,
            password=config.FIRST_SUPERUSER_PASSWORD,
            access_token=generate_token(config.FIRST_SUPERUSER, config.SECRETE_KEY),
            is_active=True,
            is_superuser=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        session.add(user)
        session.commit()
