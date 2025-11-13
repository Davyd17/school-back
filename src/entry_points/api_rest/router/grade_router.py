from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter

from app.fastapi_dependencies.grade_provider import provide_find_all_grades
from application.usecase.grade.find_all_grades import FindAllGrades
from ..response.grade.grade_response import GradeResponse
from ..response.grade.grade_response_mapper import GradeResponseMapper

router = APIRouter(prefix="/grade", tags=["grade"])

@router.get("/", response_model=List[GradeResponse])
def read_grades(usecase: FindAllGrades = Depends(provide_find_all_grades)):

    grades = usecase.execute()

    return [GradeResponseMapper.from_domain(grade) for grade in grades]
