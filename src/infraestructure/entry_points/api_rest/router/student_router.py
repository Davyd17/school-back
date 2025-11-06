from typing import List

from fastapi import APIRouter, Depends

from domain.usecase.student.student_find_all_usecase import StudentFindAllUsecase
from infraestructure.entry_points.api_rest.provider.student_provider import provide_student_find_all_usecase
from infraestructure.entry_points.api_rest.response.user.student.student_response import StudentResponse
from infraestructure.entry_points.api_rest.response.user.student.student_response_mapper import StudentResponseMapper

router = APIRouter(prefix="/student", tags=["student"])

@router.get("/", response_model=List[StudentResponse])
def read_students(usecase: StudentFindAllUsecase = Depends(provide_student_find_all_usecase)):

    students = usecase.execute()

    return [StudentResponseMapper.from_domain(student) for student in students]