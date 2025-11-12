from entry_points.api_rest.response.group.group_response import GroupResponse
from entry_points.api_rest.response.user.base.user_response import UserResponse

class StudentResponse(UserResponse):
    student_id: int
    group_response: GroupResponse


