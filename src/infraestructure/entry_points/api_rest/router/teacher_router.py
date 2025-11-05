from typing import List

from fastapi import APIRouter, Depends

from domain.usecase.teacher.tacher_find_all_usecase import TeacherFindAllUseCase
from ..provider.teacher_provider import provide_teacher_find_all_usecase
from ..response.user.teacher.teacher_response import TeacherResponse
from ..response.user.teacher.teacher_response_mapper import TeacherResponseMapper

router = APIRouter(prefix="/teacher", tags=["teacher"])

@router.get("/", response_model=List[TeacherResponse])
def read_teachers(usecase: TeacherFindAllUseCase = Depends(provide_teacher_find_all_usecase)):

    teachers = usecase.execute()

    return [TeacherResponseMapper.from_domain(teacher) for teacher in teachers]