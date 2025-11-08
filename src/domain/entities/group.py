from dataclasses import dataclass
from typing import Optional

@dataclass
class Group:
    id: Optional[int] = None
    name: str = ""