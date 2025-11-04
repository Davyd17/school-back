from dataclasses import dataclass
from typing import Optional
from ..entities.user.teacher import Teacher
from ..entities.grade import Grade

@dataclass
class Group:
    id: Optional[int] = None
    name: str = ""
    grade: Optional[Grade] = None
    teacher: Optional[Teacher] = None