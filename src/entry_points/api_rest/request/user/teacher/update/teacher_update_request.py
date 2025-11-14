from decimal import Decimal

from entry_points.api_rest.request.user.base.user_update_request import UserUpdateRequest


class TeacherUpdateRequest(UserUpdateRequest):
    salary : Decimal = None