from entry_points.api_rest.request.group.group_request import GroupRequest
from entry_points.api_rest.request.user.base.user_update_request import UserUpdateRequest


class StudentUpdateRequest(UserUpdateRequest):
    group_request : GroupRequest = None