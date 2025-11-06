from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.subject_repository_gateway import SubjectRepositoryGateway
from domain.model.entities.subject import Subject
from infraestructure.driven_adapters.SQLModel_repository.mapper.subject_model_mapper import SubjectModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.subject_model import SubjectModel


class SubjectRepository(SubjectRepositoryGateway):
    def __init__(self, session: Session):
        self.session = session
        self.model = SubjectModel

    def get_by_id(self, id: int) -> Optional[Subject]:
        pass

    def get_all(self) -> List[Subject]:

        subjects_db = self.session.exec(select(self.model)).all()

        print(f"AQUIIIIIII%%%%% {subjects_db}")

        return [SubjectModelMapper.to_domain(subject) for subject in subjects_db]

    def create(self, entity: Subject) -> Subject:
        pass

    def update(self, id: int, entity: Subject) -> Subject:
        pass

    def delete(self, id: int):
        pass