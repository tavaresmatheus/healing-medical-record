from functools import lru_cache

from fastapi import FastAPI

from app.controllers import users
from app.config import config

app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()

app.include_router(users.router)
