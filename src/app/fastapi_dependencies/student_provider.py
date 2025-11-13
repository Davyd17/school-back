from fastapi import Depends

from app.config.database_provider import session_dep
from app.fastapi_dependencies.group_provider import provide_find_group_by_id
from app.fastapi_dependencies.role_provider import provide_find_role_by_id
from application.gateway.repository.model.student_repository import StudentRepository
from application.usecase.group.find_group_by_id import FindGroupById
from application.usecase.role.find_role_by_id import FindRoleById
from application.usecase.student.create_student import CreateStudent
from application.usecase.student.find_all_students import FindAllStudents
from application.usecase.student.find_student_by_id import FindStudentById
from application.usecase.student.update_student import UpdateStudent
from infraestructure.repository.SQLModel.repository.student_repository_impl import StudentRepositoryImpl


def __provide_repository(session: session_dep) -> StudentRepository:
    return StudentRepositoryImpl(session)

def provide_find_all_students(repository:StudentRepository = Depends(__provide_repository)) \
        -> FindAllStudents:
    return FindAllStudents(repository)

def provide_create_student(repository:StudentRepository = Depends(__provide_repository),
                           find_group_by_id:FindGroupById = Depends(provide_find_group_by_id),
                           find_role_by_id:FindRoleById = Depends(provide_find_role_by_id)) \
        -> CreateStudent:

    return CreateStudent(repository,
                         find_group_by_id,
                         find_role_by_id)

def provide_update_student(repository:StudentRepository = Depends(__provide_repository)) \
        -> UpdateStudent:

    return UpdateStudent(repository)

def provide_find_student_by_id(repository:StudentRepository = Depends(__provide_repository))\
    -> FindStudentById:

    return FindStudentById(repository)