from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Permission:
    id: Optional[int] = None
    name: str = ""