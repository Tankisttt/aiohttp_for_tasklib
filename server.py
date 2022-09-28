"""aiohttp server application"""
from aiohttp import web
from endpoints import routes

app = web.Application()
app.add_routes(routes)

web.run_app(app)
