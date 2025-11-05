from decimal import Decimal
from typing import Optional

from infraestructure.entry_points.api_rest.response.user.base.user_response import UserResponse


class TeacherResponse(UserResponse):

    teacher_id : Optional[int]
    salary : Decimal
