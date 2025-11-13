from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.student_provider import provide_find_all_students, provide_create_student, provide_update_student
from application.exception.not_found_exception import NotFoundException
from application.usecase.student.create_student import CreateStudent
from application.usecase.student.find_all_students import FindAllStudents
from application.usecase.student.update_student import UpdateStudent
from entry_points.api_rest.request.group.group_request import GroupRequest
from entry_points.api_rest.request.user.student.create.student_create_mapper import StudentCreateMapper
from entry_points.api_rest.request.user.student.create.student_create import StudentCreate
from entry_points.api_rest.request.user.student.update.student_update_mapper import StudentUpdateMapper
from entry_points.api_rest.request.user.student.update.student_update_request import StudentUpdateRequest
from entry_points.api_rest.response.user.student.student_response import StudentResponse
from entry_points.api_rest.response.user.student.student_response_mapper import StudentResponseMapper

router = APIRouter(prefix="/student", tags=["student"])

@router.get("/", response_model=List[StudentResponse])
def read_students(usecase: FindAllStudents = Depends(provide_find_all_students))\
        -> List[StudentResponse]:
    students = usecase.execute()
    mapped = [StudentResponseMapper.from_domain(student) for student in students]
    return mapped

@router.post("/", response_model=StudentResponse, status_code=201)
def create_student(create: StudentCreate,
                   usecase: CreateStudent = Depends(provide_create_student))\
        -> StudentResponse:

    student = usecase.execute(StudentCreateMapper.to_domain(create))

    return StudentResponseMapper.from_domain(student)

@router.patch("/{id}", response_model=StudentResponse, status_code=200)
def update_student(id : int,
                   update_request: StudentUpdateRequest,
                   usecase: UpdateStudent = Depends(provide_update_student)):
    try:

        student_updated = usecase.execute(id, StudentUpdateMapper.to_domain(update_request))
        return StudentResponseMapper.from_domain(student_updated)

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))






