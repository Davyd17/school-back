from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime
from domain.entities.role import Role
from domain.entities.phone_number import PhoneNumber

@dataclass
class User:
    user_id: Optional[int] = None
    name: str = None
    last_name: str = None
    username: str = None
    email: str = None
    password: str = None
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    phone_numbers: list[PhoneNumber] | List[None] = field(default_factory=list)
    role: Role = None

    def get_full_name(self) -> str:
        return f"{self.name} {self.last_name}"

    def split_full_name(self, fullname: str):
        self.name = fullname.split(" ")[0]
        self.last_name = fullname.split(" ")[1]

    @staticmethod
    def get_name_from_full_name(full_name: str) -> str:
        return full_name.split(" ")[0]

    @staticmethod
    def get_last_name_from_full_name(full_name: str) -> str:
        return full_name.split(" ")[1]