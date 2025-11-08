from domain.entities.subject import Subject
from entry_points.api_rest.response.subject.subject_response import SubjectResponse


class SubjectResponseMapper:

    @staticmethod
    def from_domain(domain: Subject) -> SubjectResponse:

        return SubjectResponse(
            id=domain.id,
            name=domain.name,
            description=domain.description,
            teacher_name=domain.teacher.name
        )

    @staticmethod
    def to_domain(response: SubjectResponse) -> Subject:

        return Subject(
            id=response.id,
            name=response.name,
            description=response.description
        )