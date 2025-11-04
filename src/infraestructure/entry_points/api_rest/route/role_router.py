from fastapi import APIRouter, Depends

from typing import List

from domain.usecase.role.role_find_all_usecase import RoleFindAllUseCase
from ..provider.role_provider import find_all_usecase

from ..response.role.role_response import RoleResponse
from ..response.role.role_response_mapper import RoleResponseMapper

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/", response_model=List[RoleResponse])
def read_roles(usecase: RoleFindAllUseCase = Depends(find_all_usecase)):
     roles = usecase.execute()
     return [RoleResponseMapper.from_domain(role) for role in roles]
