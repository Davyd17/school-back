from domain.entities.user.teacher import Teacher
from entry_points.api_rest.request.user.teacher.update.teacher_update_request import TeacherUpdateRequest


class TeacherUpdateMapper:

    @staticmethod
    def from_domain(domain: Teacher) -> TeacherUpdateRequest:

        return TeacherUpdateRequest(
            name=domain.name,
            last_name=domain.last_name,
            username=domain.username,
            email=domain.email,
            password=domain.password,
            is_active=domain.is_active,
            updated_at=domain.updated_at,
            salary=domain.salary
        )

    @staticmethod
    def to_domain(request: TeacherUpdateRequest) -> Teacher:

        return Teacher(
            salary=request.salary,
            **request.model_dump(exclude_unset=True, exclude={"salary"})
        )
