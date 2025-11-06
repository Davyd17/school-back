from fastapi.params import Depends

from domain.gateway.subject_repository_gateway import SubjectRepositoryGateway
from domain.usecase.subject.subject_find_all_usecase import SubjectFindAllUseCase
from infraestructure.driven_adapters.SQLModel_repository.database.connection import session_dep
from infraestructure.driven_adapters.SQLModel_repository.repository.subject_repository import SubjectRepository


def provide_subject_repository(session: session_dep) -> SubjectRepositoryGateway:
    return SubjectRepository(session)

def provide_subject_find_all_usecase(repository: SubjectRepositoryGateway
                                     = Depends(provide_subject_repository)):
    return SubjectFindAllUseCase(repository)