from typing import List

from fastapi import APIRouter, Depends

from app.dependencies.teacher_provider import provide_find_all_teachers
from application.usecase.teacher.find_all_teachers import FindALlTeachers
from ..response.user.teacher.teacher_response import TeacherResponse
from ..response.user.teacher.teacher_response_mapper import TeacherResponseMapper

router = APIRouter(prefix="/teacher", tags=["teacher"])

@router.get("/", response_model=List[TeacherResponse])
def read_teachers(usecase: FindALlTeachers = Depends(provide_find_all_teachers)):

    teachers = usecase.execute()

    return [TeacherResponseMapper.from_domain(teacher) for teacher in teachers]