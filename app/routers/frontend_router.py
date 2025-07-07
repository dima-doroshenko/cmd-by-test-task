from fastapi.responses import HTMLResponse
from fastapi import APIRouter

from jinja2 import Environment, FileSystemLoader, select_autoescape

from app.config import BASEDIR

router = APIRouter()


env = Environment(
    loader=FileSystemLoader(BASEDIR / "templates"),
    autoescape=select_autoescape(),
)


@router.get(
    "/",
    response_class=HTMLResponse,
    include_in_schema=False,
)
def index():
    template = env.get_template("index.html")
    return template.render()
