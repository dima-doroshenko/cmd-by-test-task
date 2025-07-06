from fastapi import APIRouter

routers = APIRouter(prefix="/api/v1")

from .weather_router import router as weather_router
routers.include_router(weather_router)
