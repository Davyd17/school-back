from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.subject_repository import SubjectRepository
from domain.entities.subject import Subject
from infraestructure.repository.SQLModel.mapper.subject_model_mapper import SubjectModelMapper
from infraestructure.repository.SQLModel.model.subject_model import SubjectModel


class SubjectRepositoryImpl(SubjectRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int) -> Optional[Subject]:
        pass

    def get_all(self) -> List[Subject]:

        subjects_db = self.session.exec(select(SubjectModel)).all()

        return [SubjectModelMapper.to_domain(subject) for subject in subjects_db]

    def create(self, create: Subject) -> Subject:
        pass

    def update(self, id: int, update: Subject) -> Subject:
        pass

    def delete(self, id: int):
        pass