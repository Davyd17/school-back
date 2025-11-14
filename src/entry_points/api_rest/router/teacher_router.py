from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.fastapi_dependencies.teacher_provider import provide_find_all_teachers, provide_find_teacher_by_id, \
    provide_create_teacher
from application.exception.not_found_exception import NotFoundException
from application.usecase.teacher.create_teacher import CreateTeacher
from application.usecase.teacher.find_all_teachers import FindALlTeachers
from application.usecase.teacher.find_teacher_by_id import FindTeacherById
from ..request.user.teacher.teacher_create_mapper import TeacherCreateMapper
from ..request.user.teacher.teacher_create_request import TeacherCreateRequest
from ..response.user.teacher.teacher_response import TeacherResponse
from ..response.user.teacher.teacher_response_mapper import TeacherResponseMapper

router = APIRouter(prefix="/teacher", tags=["teacher"])

@router.get("/", response_model=List[TeacherResponse])
def read_teachers(usecase: FindALlTeachers = Depends(provide_find_all_teachers)):

    teachers = usecase.execute()

    return [TeacherResponseMapper.from_domain(teacher) for teacher in teachers]

@router.get("/{id}", response_model=TeacherResponse, status_code=200)
def read_teacher_by_id(id:int, usecase: FindTeacherById = Depends(provide_find_teacher_by_id))\
    -> TeacherResponse:

    try:
        return TeacherResponseMapper.from_domain(usecase.execute(id))

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/", response_model=TeacherResponse, status_code=201)
def create_teacher(request:TeacherCreateRequest,
                   usecase: CreateTeacher = Depends(provide_create_teacher)) -> TeacherResponse:

    try:
        created_teacher = usecase.execute(TeacherCreateMapper.to_domain(request))

        return TeacherResponseMapper.from_domain(created_teacher)


    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500)