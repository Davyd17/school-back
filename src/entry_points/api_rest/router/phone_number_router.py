from typing import List

from fastapi import APIRouter, Depends

from app.dependencies.phone_number_provider import provide_find_all_phone_numbers
from application.usecase.phone_number.find_all_phone_numbers import FindALlPhoneNumbers
from ..response.phone_number.phone_number_response import PhoneNumberResponse
from ..response.phone_number.phone_number_response_mapper import PhoneNumberResponseMapper

router = APIRouter(prefix="/phone-number", tags=["phone-number"])

@router.get("/", response_model=List[PhoneNumberResponse])
def get_phone_numbers(usecase: FindALlPhoneNumbers = Depends(provide_find_all_phone_numbers)):
    phone_numbers = usecase.execute()
    return [PhoneNumberResponseMapper.from_domain(phone_number) for phone_number in phone_numbers]
