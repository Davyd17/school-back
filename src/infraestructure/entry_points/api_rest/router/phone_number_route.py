from typing import List

from fastapi import APIRouter, Depends

from domain.usecase.phone_number.phone_number_find_all_usecase import PhoneNumberFindAllUseCase
from ..provider.phone_number_provider import get_phone_number_find_all_usecase
from ..response.phone_number.phone_number_response import PhoneNumberResponse
from ..response.phone_number.phone_number_response_mapper import PhoneNumberResponseMapper

router = APIRouter(prefix="/phone-number", tags=["phone-number"])

@router.get("/", response_model=List[PhoneNumberResponse])
def get_phone_numbers(usecase: PhoneNumberFindAllUseCase = Depends(get_phone_number_find_all_usecase)):
    phone_numbers = usecase.execute()
    return [PhoneNumberResponseMapper.from_domain(phone_number) for phone_number in phone_numbers]
