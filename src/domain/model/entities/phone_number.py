from dataclasses import dataclass
from typing import Optional
from ..entities.user import User

@dataclass
class PhoneNumber:
    id: Optional[int] = None
    ext: Optional[int] = None
    phone: str = ""
    is_active: bool = True
    user: Optional[User] = None