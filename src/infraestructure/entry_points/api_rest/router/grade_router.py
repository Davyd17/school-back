from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter

from domain.usecase.grade.grade_find_all_usecase import GradeFindAllUseCase
from ..provider.grade_provider import provide_grade_find_all_usecase
from ..response.grade.grade_response import GradeResponse
from ..response.grade.grade_response_mapper import GradeResponseMapper

router = APIRouter(prefix="/grade", tags=["grade"])

@router.get("/", response_model=List[GradeResponse])
def read_grades(usecase: GradeFindAllUseCase = Depends(provide_grade_find_all_usecase)):

    grades = usecase.execute()

    return [GradeResponseMapper.from_domain(grade) for grade in grades]
