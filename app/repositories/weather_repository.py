from typing import Any, Iterable

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.core.models import HistoryORM


class WeatherRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_record(self, city: str, data: dict[str, Any]) -> None:
        obj = HistoryORM(city=city, data=data)
        self.session.add(obj)
        await self.session.flush()

    async def get_records_count(self) -> int:
        query = select(func.count()).select_from(HistoryORM)
        return await self.session.scalar(query) or 0

    async def get_records(self, limit: int, offset: int) -> Iterable[HistoryORM]:
        query = (
            select(HistoryORM)
            .order_by(HistoryORM.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return await self.session.scalars(query)
