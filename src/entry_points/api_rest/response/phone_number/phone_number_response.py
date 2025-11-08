from typing import Optional

from pydantic import BaseModel


class PhoneNumberResponse(BaseModel):
    id: Optional[int]
    full_number: str
    is_active: bool