from dataclasses import dataclass, field
from typing import Optional, List

from ..entities.permission import Permission


@dataclass
class Role:
    id: Optional[int] = None
    name: str = ""
    description: str = ""
    permissions: List[Permission] = field(default_factory=list)