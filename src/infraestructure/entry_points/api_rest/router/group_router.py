from typing import List

from fastapi import APIRouter, Depends

from domain.usecase.group.group_find_all_usecase import GroupFindAllUseCase
from infraestructure.entry_points.api_rest.provider.group_provider import provide_group_find_all_usecase
from infraestructure.entry_points.api_rest.response.group.group_response import GroupResponse
from infraestructure.entry_points.api_rest.response.group.group_response_mapper import GroupResponseMapper

router = APIRouter(prefix="/group", tags=["group"])

@router.get("/", response_model=List[GroupResponse])
def read_groups(usecase: GroupFindAllUseCase = Depends(provide_group_find_all_usecase)):

    groups = usecase.execute()
    return [GroupResponseMapper.from_domain(group) for group in groups]