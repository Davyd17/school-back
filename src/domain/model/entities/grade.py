from dataclasses import dataclass, field
from typing import Optional, List

from domain.model.entities.group import Group


@dataclass
class Grade:
    id: Optional[int] = None
    level: str = ""
    groups: List[Group] = field(default_factory=list)