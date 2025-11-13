from typing import Optional

from application.exception.not_found_exception import NotFoundException
from application.gateway.repository.model.student_repository import StudentRepository
from application.usecase.steps.validation import step_validate_entity_exists_by_id
from application.usecase.student.find_student_by_id import FindStudentById
from application.usecase.student.student_usecase import StudentUseCase
from domain.entities.user.student import Student

class UpdateStudent(StudentUseCase):
    def __init__(self, repository: StudentRepository):
        super().__init__(repository)

    def execute(self, id: int, update_request: Student) -> Optional[Student]:

        student_found : Optional[Student] = self.repository.get_by_id(id)

        step_validate_entity_exists_by_id(student_found, Student, id)

        for key, value in update_request.__dict__.items():
            if value is not None:
                setattr(student_found, key, value)

        return self.repository.update(id, student_found)

        



