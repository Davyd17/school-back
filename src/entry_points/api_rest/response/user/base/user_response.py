from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from entry_points.api_rest.response.phone_number.phone_number_response import PhoneNumberResponse
from entry_points.api_rest.response.role.role_response import RoleResponse


class UserResponse(BaseModel):
    user_id: Optional[int] = None
    full_name: str
    username: str
    email: str
    is_active: bool
    phone_numbers: List[PhoneNumberResponse] = []
    role: RoleResponse
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


