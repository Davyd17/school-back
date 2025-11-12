from dataclasses import dataclass
from typing import Optional

from domain.entities.grade import Grade
from domain.entities.user.teacher import Teacher


@dataclass
class Group:
    id: Optional[int] = None
    name: str = ""
    grade: Optional[Grade] = None
    teacher: Optional[Teacher] = None
