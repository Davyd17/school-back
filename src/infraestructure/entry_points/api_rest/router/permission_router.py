from typing import List

from fastapi import APIRouter, Depends

from domain.usecase.permission.permission_find_all_usecase import PermissionFindAllUseCase
from ..provider.permission_provider import get_permission_find_all_usecase

from ..response.permission.permission_response import PermissionResponse
from ..response.permission.permission_response_mapper import PermissionResponseMapper

router = APIRouter(prefix="/permission", tags=["permission"])

@router.get("/", response_model=List[PermissionResponse])
def read_permissions(usecase: PermissionFindAllUseCase = Depends(get_permission_find_all_usecase)):
    permissions = usecase.execute()
    return [PermissionResponseMapper.from_domain(permission) for permission in permissions]