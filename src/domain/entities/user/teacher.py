from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from decimal import Decimal

from ..user.user import User

@dataclass
class Teacher(User):
    teacher_id: Optional[int] = None
    salary: Decimal = Decimal("0.00")