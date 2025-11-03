from dataclasses import dataclass
from typing import Optional


@dataclass
class Role:
    id: Optional[int] = None
    name: str = ""
    description: str = ""
