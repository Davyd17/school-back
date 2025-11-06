from typing import List

from pydantic import BaseModel

from infraestructure.entry_points.api_rest.response.group.group_response import GroupResponse


class GradeResponse(BaseModel):
    id: int
    level: str
    groups: List[GroupResponse]