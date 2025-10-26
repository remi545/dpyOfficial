import os
from typing import Any
from beanie import init_beanie  # type: ignore
from pymongo.asynchronous.mongo_client import AsyncMongoClient

from .models import User


MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://dpy:password@db:27017/dpy_official?authSource=admin")
DATABASE_NAME = "dpy_official"


client: AsyncMongoClient[Any] = AsyncMongoClient(MONGODB_URL)

async def init_db():
    """Beanieを初期化"""
    await init_beanie(
        database=client[DATABASE_NAME],
        document_models=[User]
    )

async def close_db():
    """データベース接続を閉じる"""
    await client.close()
