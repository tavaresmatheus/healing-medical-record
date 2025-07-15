from functools import lru_cache
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .controllers import users
from .database import database
from .config import config

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     database.create_db()
#     yield

# app = FastAPI(lifespan=lifespan)
app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()

app.include_router(users.router)
