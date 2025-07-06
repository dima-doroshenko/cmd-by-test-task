from typing import Any

from urllib.parse import urljoin
from collections import namedtuple

from fastapi import HTTPException

import aiohttp

from app.schemas.weather_schemas import WeatherInfoSchema
from app.core.requests import make_request
from app.config import settings


_Coordinates = namedtuple("_Coordinates", ("lat", "lon"))


class OpenWeatherMapClient:

    def __init__(self, aiohttp_session: aiohttp.ClientSession):
        self.aiohttp_session = aiohttp_session

    async def _make_request(self, url: str, **params: Any):
        url = urljoin(settings.weather_api.base_url, url)
        params = params.copy()
        params["appid"] = settings.weather_api.api_key
        data = await make_request(
            url=url,
            aiohttp_session=self.aiohttp_session,
            params=params,
        )
        if data is None:
            raise HTTPException(status_code=400, detail="Bad request")
        return data

    async def get_coordinates_by_city(self, city: str) -> _Coordinates:
        data = await self._make_request("geo/1.0/direct", q=city)
        return _Coordinates(data[0]["lat"], data[0]["lon"])

    async def get_weather_by_coordinates(self, coordinates: _Coordinates) -> WeatherInfoSchema:
        data = await self._make_request(
            "data/3.0/onecall", lat=coordinates.lat, lon=coordinates.lon
        )
        return WeatherInfoSchema(
            temp=data["current"]["temp"] - 273.15,
            humidity=data["current"]["humidity"],
            pressure=data["current"]["pressure"],
            description=data["current"]["weather"]["description"],
        )

    async def get_weather_by_city(self, city: str) -> WeatherInfoSchema:
        coordinates = await self.get_coordinates_by_city(city=city)
        return await self.get_weather_by_coordinates(coordinates=coordinates)
