from dataclasses import dataclass
from typing import Optional

from ..group import Group
from ..user.user import User

@dataclass
class Student(User):
    student_id: Optional[int] = None
    group: Group = None
