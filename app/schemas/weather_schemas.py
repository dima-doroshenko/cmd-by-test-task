from typing import Any, Self

from datetime import datetime

from pydantic import BaseModel, Field


class WeatherInfoSchema(BaseModel):
    temp: float = Field(examples=[22])
    humidity: float = Field(examples=[63])
    pressure: int = Field(examples=[993])
    description: str = Field(examples=["Broken clouds"])


class WeatherRequestRecordSchema(BaseModel):
    city: str = Field(examples=["Минск"])
    data: WeatherInfoSchema
    created_at: datetime
