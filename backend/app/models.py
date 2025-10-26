from beanie import Document
from pydantic import Field, ConfigDict
from datetime import datetime

class User(Document):
    """ユーザーモデル（例として残す）"""
    name: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "users"
        
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "created_at": "2025-01-01T00:00:00"
            }
        }
    )
