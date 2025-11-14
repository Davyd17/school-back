from fastapi import Depends
from sqlmodel import Session

from app.config.database_provider import session_dep
from application.gateway.repository.model.teacher_repository import TeacherRepository
from application.usecase.teacher.create_teacher import CreateTeacher
from application.usecase.teacher.find_all_teachers import FindALlTeachers
from application.usecase.teacher.find_teacher_by_id import FindTeacherById
from infraestructure.repository.SQLModel.repository.teacher_repository_impl import TeacherRepositoryImpl

def __provide_repository(session: session_dep) -> TeacherRepository:
        return TeacherRepositoryImpl(session)

def provide_find_all_teachers(repository: TeacherRepository
                                     = Depends(__provide_repository)) -> FindALlTeachers:
    return FindALlTeachers(repository)

def provide_find_teacher_by_id(repository: TeacherRepository
                               = Depends(__provide_repository)) -> FindTeacherById:

    return FindTeacherById(repository)

def provide_create_teacher(repository: TeacherRepository
                           = Depends(__provide_repository)) -> CreateTeacher:
    return CreateTeacher(repository)