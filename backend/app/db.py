import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://dpy:password@db:5432/dpy_official")
engine = create_async_engine(DATABASE_URL, echo=True)

async def get_session():
    async with AsyncSession(engine) as session:
        yield session
