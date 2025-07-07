from typing import Any

import aiohttp


async def make_request(
    url: str,
    aiohttp_session: aiohttp.ClientSession,
    method: str = "get",
    params: dict[str, Any] | None = None,
    json: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    ssl: bool = False,
) -> dict[str, Any] | None:
    try:
        async with aiohttp_session.request(
            method=method,
            url=url,
            params=params,
            json=json,
            headers=headers,
            ssl=ssl,
        ) as response:
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientError:
        return
