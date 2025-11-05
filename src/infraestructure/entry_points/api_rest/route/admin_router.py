from typing import List

from fastapi import APIRouter, Depends

from domain.usecase.admin.admin_find_all_use_case import AdminFindAllUseCase
from ..provider.admin_provider import get_admin_find_all_usecase
from ..response.admin.admin_response import AdminResponse
from ..response.admin.admin_response_mapper import AdminResponseMapper

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/", response_model=List[AdminResponse])
def read_admins(usecase: AdminFindAllUseCase = Depends(get_admin_find_all_usecase)):
    admins = usecase.execute()
    return [AdminResponseMapper.from_domain(admin) for admin in admins]