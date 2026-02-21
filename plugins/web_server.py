from aiohttp import web

async def web_server():
    web_app = web.Application()
    return web_app
