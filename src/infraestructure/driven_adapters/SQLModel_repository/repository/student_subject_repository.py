from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.student_subject_repository_gateway import StudentSubjectRepositoryGateway
from domain.model.entities.student_subject import StudentSubject
from infraestructure.driven_adapters.SQLModel_repository.mapper.student_subject_model_mapper import \
    StudentSubjectModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.student_subject_model import StudentSubjectModel


class StudentSubjectRepository(StudentSubjectRepositoryGateway):
    def __init__(self, session: Session):
        self.session__ = session
        self.model__ = StudentSubjectModel

    def get_by_id(self, id: int) -> Optional[StudentSubject]:
        pass

    def get_all(self) -> List[StudentSubject]:

        students_subjects_model = self.session__.exec(select(self.model__)).all()
        return[StudentSubjectModelMapper.to_domain(student) for student in students_subjects_model]


    def create(self, entity: StudentSubject) -> StudentSubject:
        pass

    def update(self, id: int, entity: StudentSubject) -> StudentSubject:
        pass

    def delete(self, id: int):
        pass