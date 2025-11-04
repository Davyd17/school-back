from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    full_name: str
    username: str
    email: str
    is_active: bool
    phone_numbers: List[str] = []
    role: str
    created_at: datetime
    updated_at: datetime | None
