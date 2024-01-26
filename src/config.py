import os
from pathlib import Path

from dotenv import load_dotenv

current_dir = Path(__file__).parent
load_dotenv(dotenv_path=current_dir.parent / ".env")


class Config:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRETE_KEY = "1234567890"

    FIRST_SUPERUSER = "admin"
    FIRST_SUPERUSER_PASSWORD = "admin"
    FIRST_SUPERUSER_EMAIL = "admin@mail.com"
