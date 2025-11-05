from dataclasses import dataclass
from typing import Optional
from ..user.user import User

@dataclass
class Admin(User):
    admin_id: Optional[int] = None