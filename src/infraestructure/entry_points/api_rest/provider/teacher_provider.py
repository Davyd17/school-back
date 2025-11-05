from fastapi import Depends

from domain.gateway.teacher_repository_gateway import TeacherRepositoryGateway
from domain.usecase.teacher.tacher_find_all_usecase import TeacherFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.teacher_repository import TeacherRepository

def provide_teacher_repository(session: session_dep) -> TeacherRepositoryGateway:
        return TeacherRepository(session)

def provide_teacher_find_all_usecase(repository: TeacherRepositoryGateway
                                     = Depends(provide_teacher_repository)) -> TeacherFindAllUseCase:
    return TeacherFindAllUseCase(repository)