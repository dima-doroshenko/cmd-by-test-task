from typing import Any, Self

from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class WeatherInfoSchema(BaseModel):
    temp: int = Field(examples=[22])
    humidity: int = Field(examples=[63])
    pressure: int = Field(examples=[993])
    description: str = Field(examples=["Broken clouds"])

    @model_validator(mode="before")
    def validate_model(self) -> Self:
        if isinstance(self, dict):
            self["temp"] = round(self["temp"])
        else:
            self.temp = round(self.temp)
        return self


class WeatherRequestRecordSchema(BaseModel):
    city: str = Field(examples=["Минск"])
    data: WeatherInfoSchema
    created_at: datetime
