import uvicorn
from fastapi import FastAPI

from api.demo.routes import demo
from api.users.routes import users

__version__ = "1.0.0"

app = FastAPI(
    title="Demo Application",
    description="Some description for the demo application could be here",
    version=__version__,
)
app.include_router(users, prefix="/users")
app.include_router(demo, prefix="/demo")

uvicorn.run(app)
