from typing import List, Optional

from sqlmodel import Session, select

from application.gateway.repository.model.student_subject import StudentSubjectRepository
from domain.entities.student_subject import StudentSubject
from infraestructure.repository.SQLModel.mapper.student_subject_model_mapper import StudentSubjectModelMapper
from infraestructure.repository.SQLModel.model.student_subject_model import StudentSubjectModel


class StudentSubjectRepositoryImpl(StudentSubjectRepository):
    def __init__(self, session: Session):
        self.session__ = session

    def get_by_id(self, id: int) -> Optional[StudentSubject]:
        pass

    def get_all(self) -> List[StudentSubject]:

        students_subjects_model = self.session__.exec(select(StudentSubjectModel)).all()
        return[StudentSubjectModelMapper.to_domain(student_subject) for student_subject in students_subjects_model]


    def create(self, create: StudentSubject) -> StudentSubject:
        pass

    def update(self, id: int, update: StudentSubject) -> StudentSubject:
        pass

    def delete(self, id: int):
        pass