from typing import List, Optional

from sqlmodel import select, Session

from application.gateway.repository.model.student_repository import StudentRepository
from domain.entities.user.student import Student
from infraestructure.repository.SQLModel.mapper.student_model_mapper import StudentModelMapper
from infraestructure.repository.SQLModel.model.user_model.student_model import StudentModel


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, session: Session):
        self.session__ = session

    def get_by_id(self, id: int) -> Optional[Student]:
        pass

    def get_all(self) -> List[Student]:

        students_model = self.session__.exec(select(StudentModel)).all()

        return [StudentModelMapper.to_domain(student) for student in students_model]

    def create(self, create: Student) -> Student:
        model = StudentModelMapper.from_domain(create)
        self.session__.add(model)
        self.session__.commit()
        self.session__.refresh(model)
        return StudentModelMapper.to_domain(model)

    def update(self, id: int, update: Student) -> Student:
        pass

    def delete(self, id: int):
        pass