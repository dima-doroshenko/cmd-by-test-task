from dotenv import load_dotenv
import os

from pydantic_settings import BaseSettings
from pydantic import BaseModel

load_dotenv()


class DB(BaseModel):
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    db: str = os.getenv("POSTGRES_DB")
    host: str = os.getenv("POSTGRES_HOST")
    port: int = os.getenv("POSTGRES_PORT")


class Settings(BaseSettings):
    db: DB = DB()


settings = Settings()
