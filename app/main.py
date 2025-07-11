from fastapi import FastAPI
from .controllers import users
from .database import database
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
