from typing import List

from fastapi import APIRouter, Depends

from app.dependencies.permission_provider import provide_find_all_permissions
from application.usecase.permission.find_all_permissions import FindAllPermissions
from ..response.permission.permission_response import PermissionResponse
from ..response.permission.permission_response_mapper import PermissionResponseMapper

router = APIRouter(prefix="/permission", tags=["permission"])

@router.get("/", response_model=List[PermissionResponse])
def read_permissions(usecase: FindAllPermissions = Depends(provide_find_all_permissions)):
    permissions = usecase.execute()
    return [PermissionResponseMapper.from_domain(permission) for permission in permissions]