from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Subject:
    id: Optional[int] = None
    name: str = ""
    description: str = ""
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    teacher_id: Optional[int] = None