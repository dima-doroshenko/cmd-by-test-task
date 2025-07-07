from typing import Literal

from pydantic import BaseModel


class HTTPExceptionModel(BaseModel):
    detail: str


def BadResponses(
    *status_codes: int,
) -> dict[
    int,
    dict[
        Literal["model"],
        type[HTTPExceptionModel],
    ],
]:
    return {status_code: {"model": HTTPExceptionModel} for status_code in status_codes}
