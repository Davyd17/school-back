from typing import Optional

from application.gateway.repository.model.teacher_repository import TeacherRepository
from application.usecase.steps.validation import step_validate_entity_exists_by_id
from application.usecase.teacher.teacher_usecase import TeacherUseCase
from domain.entities.user.teacher import Teacher


class FindTeacherById(TeacherUseCase):
    def __init__(self, repository: TeacherRepository):
        super().__init__(repository)

    def execute(self, id:int) -> Optional[Teacher]:

        teacher_found = self._repository.get_by_id(id)
        step_validate_entity_exists_by_id(teacher_found, Teacher, id)

        return teacher_found