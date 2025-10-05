from typing import Optional, List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from pydantic import BaseModel
from .models import User
from .db import get_session

class UserResponse(BaseModel):
    id: Optional[int]
    name: str

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "DPY Official API is running."}

@router.post("/users", response_model=UserResponse)
async def create_user(name: str, session: AsyncSession = Depends(get_session)) -> UserResponse:
    user = User(name=name)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return UserResponse(id=user.id, name=user.name)

@router.get("/users", response_model=List[UserResponse])
async def list_users(session: AsyncSession = Depends(get_session)) -> List[UserResponse]:
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [UserResponse(id=u.id, name=u.name) for u in users]
