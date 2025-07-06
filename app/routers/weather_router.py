from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
import aiohttp

from app.dependencies import get_aiohttp_session, get_session
from app.schemas.weather_schemas import WeatherInfoSchema, WeatherRequestRecordSchema
from app.schemas.pagination_schemas import PaginationQuery, PaginationResult
from app.services.weather_service import WeatherService
from app.exc import BadResponses

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/history")
async def get_weather_request_records(
    pagination: Annotated[PaginationQuery, Depends()],
    session: AsyncSession = Depends(get_session),
) -> PaginationResult[WeatherRequestRecordSchema]:
    weather_service = WeatherService(session=session)
    return await weather_service.get_history(pagination=pagination)


@router.get(
    "/{city}",
    responses=BadResponses(400),
)
async def get_weather_by_city(
    city: str,
    session: AsyncSession = Depends(get_session),
    aiohttp_session: aiohttp.ClientSession = Depends(get_aiohttp_session),
) -> WeatherInfoSchema:
    weather_service = WeatherService(session=session, aiohttp_session=aiohttp_session)
    return await weather_service.get_weather(city=city)
