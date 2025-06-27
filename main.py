import os
import contextlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from autumn import Autumn  # type: ignore

from routes import router

autumn = Autumn(token=os.environ["AUTUMN_SECRET_KEY"])

app = FastAPI(debug=True)

templates = Jinja2Templates(directory="templates")


@contextlib.asynccontextmanager
async def lifespan(_):
    yield
    await autumn.close()


# CORS must be configured correctly.
# You must allow the GET, POST and OPTIONS methods at a minimum.
# Pass your frontend url here.
ORIGINS = ["http://localhost:8000"]

# Note this example uses FastAPI, but can use Litestar, Starlette, or any other ASGI framework
# that supports mounting ASGI apps.
app = FastAPI(debug=True, lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"))
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.state.templates = templates
app.state.autumn = autumn
