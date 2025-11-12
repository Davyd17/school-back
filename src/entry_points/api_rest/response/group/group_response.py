from pydantic import BaseModel

from entry_points.api_rest.response.grade.grade_response import GradeResponse
from entry_points.api_rest.response.user.teacher.teacher_response import TeacherResponse


class GroupResponse(BaseModel):
    id : int
    name : str
    grade_response : GradeResponse
    teacher_response : TeacherResponse
