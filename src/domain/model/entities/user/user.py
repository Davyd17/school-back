from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime
from domain.model.entities.role import Role
from domain.model.entities.phone_number import PhoneNumber

@dataclass
class User:
    user_id: Optional[int] = None
    name: str = ""
    last_name: str = ""
    username: str = ""
    email: str = ""
    password: str = ""
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    phone_numbers: List[PhoneNumber] | List[None] = field(default_factory=List)
    role: Optional[Role] = None

    def get_full_name(self) -> str:
        return f"{self.name} {self.last_name}"