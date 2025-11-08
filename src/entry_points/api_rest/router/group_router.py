from typing import List

from fastapi import APIRouter, Depends

from app.dependencies.group_provider import provide_find_all_groups
from application.usecase.group.find_all_groups import FindAllGroups
from entry_points.api_rest.response.group.group_response import GroupResponse
from entry_points.api_rest.response.group.group_response_mapper import GroupResponseMapper

router = APIRouter(prefix="/group", tags=["group"])

@router.get("/", response_model=List[GroupResponse])
def read_groups(usecase: FindAllGroups = Depends(provide_find_all_groups)):
    groups = usecase.execute()
    return [GroupResponseMapper.from_domain(group) for group in groups]
