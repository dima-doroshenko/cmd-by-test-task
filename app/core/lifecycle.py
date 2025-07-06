from fastapi import FastAPI

import aiohttp


class Lifecycle:

    def __init__(self, a: FastAPI):
        self.app = a

    async def on_startup(self):
        await self._aiohttp_startup()

    async def on_shutdown(self):
        await self._aiohttp_shutdown()

    async def _aiohttp_startup(self):
        self.aiohttp_session = aiohttp.ClientSession()
        self.app.state.aiohttp_session = self.aiohttp_session

    async def _aiohttp_shutdown(self):
        try:
            if self.aiohttp_session and not self.aiohttp_session.closed:
                await self.aiohttp_session.close()
        except:
            ...
    