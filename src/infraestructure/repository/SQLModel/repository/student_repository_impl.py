from typing import List, Optional

from sqlmodel import select, Session

from application.gateway.repository.model.student_repository import StudentRepository
from domain.entities.user.student import Student
from infraestructure.repository.SQLModel.mapper.student_model_mapper import StudentModelMapper
from infraestructure.repository.SQLModel.model.user_model.student_model import StudentModel


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, session: Session):
        self.__session = session

    def get_by_id(self, id: int) -> Optional[Student]:

        statement = select(StudentModel).where(StudentModel.student_id == id)
        return StudentModelMapper.to_domain(self.__session.exec(statement).first())

    def get_all(self) -> List[Student]:

        students_model = self.__session.exec(select(StudentModel)).all()
        return [StudentModelMapper.to_domain(student) for student in students_model]

    def create(self, create: Student) -> Student:

        student_model, user_model = StudentModelMapper.from_domain(create)

        self.__session.add(user_model)
        self.__session.flush()

        student_model.user_id = user_model.id

        self.__session.add(student_model)
        self.__session.commit()
        self.__session.refresh(student_model)

        return StudentModelMapper.to_domain(student_model)

    def update(self, id: int, update: Student) -> Optional[Student]:

        new_student_model, new_user_model = StudentModelMapper.from_domain(update)

        self.__session.merge(new_user_model)
        student_merged = self.__session.merge(new_student_model)
        self.__session.commit()
        self.__session.refresh(student_merged)
        self.__session.refresh(student_merged.user)

        return StudentModelMapper.to_domain(student_merged)


    def delete(self, id: int):
        pass