from fastapi import APIRouter, Depends
from typing import List
from domain.usecase.role_crud_usecase import RoleCrudUseCase
from ..provider.role_provider import get_role_usecase

from ..response.role.role_response import RoleResponse
from ..response.role.role_response_mapper import RoleResponseMapper

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/", response_model=List[RoleResponse])
def read_roles(usecase: RoleCrudUseCase = Depends(get_role_usecase)):
    roles = usecase.get_all()
    return [RoleResponseMapper.from_domain(role) for role in roles]



