from fastapi import APIRouter, Depends

from typing import List

from app.dependencies.role_provider import provide_find_all_roles
from application.usecase.role.find_all_roles import FindAllRoles
from ..response.role.role_response import RoleResponse
from ..response.role.role_response_mapper import RoleResponseMapper

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/", response_model=List[RoleResponse])
def read_roles(usecase: FindAllRoles = Depends(provide_find_all_roles)):
     roles = usecase.execute()
     return [RoleResponseMapper.from_domain(role) for role in roles]
