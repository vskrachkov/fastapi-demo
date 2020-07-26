import uvicorn
from fastapi import FastAPI, HTTPException

from api.demo.endpoints import demo
from api.exception_handlers import server_error_handler, http_exception_handler
from api.users.endpoints import users

__version__ = "1.0.0"

app = FastAPI(
    title="Demo Application",
    description="Some description for the demo application could be here",
    version=__version__,
)

app.add_exception_handler(Exception, server_error_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(users, prefix="/users")
app.include_router(demo, prefix="/demo")

uvicorn.run(app)
