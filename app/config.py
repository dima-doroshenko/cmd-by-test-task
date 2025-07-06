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

    @property
    def url(self):
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.db}"
        )


class WeatherAPI(BaseModel):
    api_key: str = os.getenv("OPEN_WEATHER_MAP_API_KEY")
    base_url: str = os.getenv("OPEN_WEATHER_MAP_BASE_URL")


class Settings(BaseSettings):
    db: DB = DB()
    weather_api: WeatherAPI = WeatherAPI()


settings = Settings()
