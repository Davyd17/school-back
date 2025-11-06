from fastapi import Depends

from domain.gateway.student_repository_gateway import StudentRepositoryGateway
from domain.gateway.student_subject_repository_gateway import StudentSubjectRepositoryGateway
from domain.usecase.student.student_find_all_usecase import StudentFindAllUsecase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.student_repository import StudentRepository


def provide_student_repository(session: session_dep) -> StudentSubjectRepositoryGateway:
    return StudentRepository(session)

def provide_student_find_all_usecase(repository: StudentRepositoryGateway
                                     = Depends(provide_student_repository)) -> StudentFindAllUsecase:
    return StudentFindAllUsecase(repository)