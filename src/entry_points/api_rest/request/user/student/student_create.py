from entry_points.api_rest.request.group.group_request import GroupRequest
from entry_points.api_rest.request.user.base.user_create import UserCreate


class StudentCreate(UserCreate):
    group_request : GroupRequest
