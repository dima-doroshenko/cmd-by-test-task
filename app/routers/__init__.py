from fastapi import APIRouter

api_routers = APIRouter(prefix="/api/v1")

from .weather_router import router as weather_router
api_routers.include_router(weather_router)


routers = APIRouter()

routers.include_router(api_routers)

from .frontend_router import router as frontend_router
routers.include_router(frontend_router)
