from typing import List

from fastapi import APIRouter, Depends

from domain.usecase.user.user_find_all_usecase import UserFindAllUseCase
from ..provider.user_provider import get_user_find_all_usecase
from ..response.user.user_response import UserResponse
from ..response.user.user_response_mapper import UserResponseMapper

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=List[UserResponse])
def read_users(usecase: UserFindAllUseCase = Depends(get_user_find_all_usecase)) -> List[UserResponse]:
    users = usecase.execute()
    return [UserResponseMapper.from_domain(user) for user in users]