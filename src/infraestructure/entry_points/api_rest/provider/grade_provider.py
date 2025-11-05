from fastapi import Depends

from domain.gateway.grade_repository_gateway import GradeRepositoryGateway
from domain.usecase.grade.grade_find_all_usecase import GradeFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.grade_repository import GradeRepository


def provide_grade_repository(session: session_dep) -> GradeRepositoryGateway:
    return GradeRepository(session)

def provide_grade_find_all_usecase(repository: GradeRepositoryGateway
                                   = Depends(provide_grade_repository)):
    return GradeFindAllUseCase(repository)