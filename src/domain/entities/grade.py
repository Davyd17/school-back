from dataclasses import dataclass
from typing import Optional

@dataclass
class Grade:
    id: Optional[int] = None
    level: str = ""