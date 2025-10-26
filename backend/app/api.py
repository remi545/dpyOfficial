from typing import List
from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from .models import User

router = APIRouter(prefix="/api")

@router.post("/users", response_model=User)
async def create_user(name: str) -> User:
    """新しいユーザーを作成"""
    user = User(name=name)
    await user.insert()
    return user

@router.get("/users", response_model=List[User])
async def list_users() -> List[User]:
    """ユーザー一覧を取得"""
    users = await User.find_all().to_list()
    return users

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: PydanticObjectId) -> User:
    """特定のユーザーを取得"""
    user = await User.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: PydanticObjectId):
    """ユーザーを削除"""
    user = await User.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"message": "User deleted successfully"}
