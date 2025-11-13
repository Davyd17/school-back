from datetime import datetime

from pydantic import BaseModel


class UserUpdateRequest(BaseModel):
    name:str = None
    last_name: str = None
    username: str = None
    email: str = None
    password: str = None
    is_active: bool = None
    updated_at:datetime = datetime.now()

