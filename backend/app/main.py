from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import engine
from sqlmodel import SQLModel
from .api import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)
