from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime
from domain.model.entities.role import Role
from domain.model.entities.phone_number import PhoneNumber

@dataclass
class User:
    id: Optional[int] = None
    name: str = ""
    last_name: str = ""
    username: str = ""
    email: str = ""
    password: str = ""
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    phone_numbers: List[PhoneNumber] = field(default_factory=list)
    role: Optional[Role] = None