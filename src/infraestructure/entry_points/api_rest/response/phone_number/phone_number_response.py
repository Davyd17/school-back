from pydantic import BaseModel


class PhoneNumberResponse(BaseModel):
    id: int
    full_number: str
    is_active: bool