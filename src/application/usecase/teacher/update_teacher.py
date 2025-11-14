from typing import Optional

from application.gateway.repository.model.teacher_repository import TeacherRepository
from application.usecase.steps.validation import step_validate_entity_exists_by_id
from application.usecase.teacher.teacher_usecase import TeacherUseCase
from domain.entities.user.teacher import Teacher


class UpdateTeacher(TeacherUseCase):
    def __init__(self, repository: TeacherRepository):
        super().__init__(repository)

    def execute(self, id:int, update_request:Teacher) -> Teacher:

        teacher_found : Optional[Teacher] = self._repository.get_by_id(id)
        step_validate_entity_exists_by_id(teacher_found, Teacher, id)

        for key, value in update_request.__dict__.items():
            if value is not None:
                setattr(teacher_found, key, value)

        return self._repository.update(teacher_found)

