from fastapi import Request

import aiohttp

from app.core.database import SessionLocal


def get_aiohttp_session(request: Request) -> aiohttp.ClientSession:
    return request.app.state.aiohttp_session

async def get_session():
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as err:
            await session.rollback()
            raise err
        finally:
            await session.close()