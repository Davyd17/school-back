from dataclasses import dataclass
from typing import Optional

@dataclass
class PhoneNumber:
    id: Optional[int] = None
    ext: Optional[int] = None
    phone: str = ""
    is_active: bool = True
    contact: Optional["User"] = None

    def get_full_number(self) -> str:
        if self.ext:
            return f"+{self.ext} {self.phone}"
        return self.phone