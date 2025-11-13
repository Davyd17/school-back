from typing import Optional

from application.gateway.repository.model.student_repository import StudentRepository
from application.usecase.steps.validation import step_validate_entity_exists_by_id
from application.usecase.student.student_usecase import StudentUseCase
from domain.entities.user.student import Student


class FindStudentById(StudentUseCase):
    def __init__(self, repository: StudentRepository):
        super().__init__(repository)

    def execute(self, id) -> Optional[Student]:

        student_found: Optional[Student] = self.repository.get_by_id(id)
        step_validate_entity_exists_by_id(student_found, Student, id)

        return student_found