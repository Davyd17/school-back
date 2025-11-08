# python
from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

from ..user.user import User

@dataclass
class Teacher(User):
    teacher_id: Optional[int] = None
    salary: Decimal = Decimal("0.00")