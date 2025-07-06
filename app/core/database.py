from app.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.db.url)
SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=True)


class Base(DeclarativeBase): ...
