from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from domain.model.entities.user.teacher import Teacher


@dataclass
class Subject:
    id: Optional[int] = None
    name: str = ""
    description: str = ""
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    teacher: Optional[Teacher] = None