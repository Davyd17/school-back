from typing import List, Optional

from sqlmodel import Session, select

from domain.gateway.student_subject_repository_gateway import StudentSubjectRepositoryGateway
from domain.model.entities.user.student import Student
from infraestructure.driven_adapters.SQLModel_repository.mapper.student_model_mapper import StudentModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.user_model.student_model import StudentModel

class StudentRepository(StudentSubjectRepositoryGateway):
    def __init__(self, session: Session):
        self.session__ = session
        self.model__ = StudentModel

    def get_by_id(self, id: int) -> Optional[Student]:
        pass

    def get_all(self) -> List[Student]:

        students_model = self.session__.exec(select(self.model__)).all()

        return [StudentModelMapper.to_domain(student) for student in students_model]

    def create(self, entity: Student) -> Student:
        pass

    def update(self, id: int, entity: Student) -> Student:
        pass

    def delete(self, id: int):
        pass