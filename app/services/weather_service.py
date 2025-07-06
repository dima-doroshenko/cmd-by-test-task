import aiohttp

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.weather_repository import WeatherRepository
from app.clients.open_weather_map import OpenWeatherMapClient
from app.schemas.weather_schemas import WeatherInfoSchema, WeatherRequestRecordSchema
from app.schemas.pagination_schemas import PaginationQuery, PaginationResult


class WeatherService:

    def __init__(
        self,
        session: AsyncSession,
        aiohttp_session: aiohttp.ClientSession = None,
    ):
        self.session = session
        self.aiohttp_session = aiohttp_session
        self.repo = WeatherRepository(session=session)
        self.weather_client = OpenWeatherMapClient(aiohttp_session=aiohttp_session)

    async def get_weather(self, city: str) -> WeatherInfoSchema:
        current_weather = await self.weather_client.get_weather_by_city(city=city)
        await self.repo.create_record(city=city, data=current_weather.model_dump())
        return current_weather

    async def get_history(
        self,
        pagination: PaginationQuery,
    ) -> PaginationResult[WeatherRequestRecordSchema]:
        total_count = await self.repo.get_records_count()
        items = await self.repo.get_records(
            limit=pagination.size, offset=(pagination.page - 1) * pagination.size
        )
        return PaginationResult(
            page=pagination.page,
            size=pagination.size,
            total_items=total_count,
            items=items,
        )
