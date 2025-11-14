from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserUpdateRequest(BaseModel):
    name:str = None
    last_name: str = None
    username: str = None
    email: EmailStr = None
    password: str = None
    is_active: bool = None
    updated_at:datetime = None

