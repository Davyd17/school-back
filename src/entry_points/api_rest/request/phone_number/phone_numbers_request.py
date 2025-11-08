from pydantic import BaseModel


class PhoneNumbersRequest(BaseModel):
    contact: str