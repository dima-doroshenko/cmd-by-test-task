from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

from app.core.lifecycle import Lifecycle
from app.routers import routers
from app.config import BASEDIR


app = FastAPI()


def configure_cors(a: FastAPI) -> None:
    a.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def setup_routers(a: FastAPI) -> None:
    a.include_router(router=routers)


def mount_static(a: FastAPI) -> None:
    a.mount(
        "/static",
        StaticFiles(directory=BASEDIR / "templates" / "static"),
        name="static",
    )


@asynccontextmanager
async def lifespan(a: FastAPI):
    lifecycle = Lifecycle(a)
    await lifecycle.on_startup()
    try:
        yield
    finally:
        await lifecycle.on_shutdown()


def create_app() -> FastAPI:
    app = FastAPI(
        title="GetWeather",
        lifespan=lifespan,
    )

    configure_cors(app)
    setup_routers(app)
    mount_static(app)

    return app


app = create_app()
