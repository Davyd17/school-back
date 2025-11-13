from typing import List

from fastapi import APIRouter, Depends

from app.fastapi_dependencies.user_provider import provide_find_all_users
from application.usecase.user.find_all_users import FindAllUsers
from entry_points.api_rest.response.user.base.user_response import UserResponse
from entry_points.api_rest.response.user.base.user_response_mapper import UserResponseMapper

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=List[UserResponse])
def read_users(usecase: FindAllUsers = Depends(provide_find_all_users)) -> List[UserResponse]:
    users = usecase.execute()
    return [UserResponseMapper.from_domain(user) for user in users]