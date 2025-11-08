from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from domain.entities.role import Role
from entry_points.api_rest.response.phone_number.phone_number_response import PhoneNumberResponse

class UserResponse(BaseModel):
    user_id: Optional[int] = None
    name: str
    last_name: str
    username: str
    email: str
    is_active: bool
    phone_numbers: List[PhoneNumberResponse] = []
    role: Role
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


