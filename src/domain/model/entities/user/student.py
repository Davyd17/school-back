from dataclasses import dataclass, field
from typing import Optional, Dict
from decimal import Decimal

from ..user.user import User

@dataclass
class Student(User):
    student_id: Optional[int] = None
    subject_averages: Dict[int, Decimal] = field(default_factory=dict)
    group_id: Optional[int] = None
