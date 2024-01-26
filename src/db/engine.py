from sqlalchemy import create_engine
from src.config import Config

config = Config()

if config.DATABASE_URI is None:
    raise Exception("DATABASE_URI is not set")

engine = create_engine(config.DATABASE_URI)
