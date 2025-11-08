from typing import List

from fastapi import APIRouter, Depends

from app.dependencies.admin_provider import provide_find_all_admins
from application.usecase.admin.find_all_admins import FindAllAdmins
from entry_points.api_rest.response.user.admin.admin_response import AdminResponse
from entry_points.api_rest.response.user.admin.admin_response_mapper import AdminResponseMapper

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/", response_model=List[AdminResponse])
def read_admins(usecase: FindAllAdmins = Depends(provide_find_all_admins)):
    admins = usecase.execute()
    return [AdminResponseMapper.from_domain(admin) for admin in admins]