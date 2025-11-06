from dataclasses import dataclass, field
from typing import Optional, Dict
from decimal import Decimal

from ..group import Group
from ..user.user import User

@dataclass
class Student(User):
    student_id: Optional[int] = None
    group: Optional[Group] = None
