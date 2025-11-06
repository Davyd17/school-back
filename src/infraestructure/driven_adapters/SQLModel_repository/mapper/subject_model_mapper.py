from domain.model.entities.subject import Subject
from infraestructure.driven_adapters.SQLModel_repository.mapper.teacher_model_mapper import TeacherModelMapper
from infraestructure.driven_adapters.SQLModel_repository.model.subject_model import SubjectModel


class SubjectModelMapper:

    @staticmethod
    def from_domain(domain: Subject) -> SubjectModel:

        return SubjectModel(
            id=domain.id,
            name=domain.name,
            description=domain.description,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
            teacher_id=domain.teacher.teacher_id,
            teacher=TeacherModelMapper.from_domain(domain.teacher)
        )

    @staticmethod
    def to_domain(model: SubjectModel) -> Subject:

        return Subject(
            id=model.id,
            name=model.name,
            description=model.description,
            created_at=model.created_at,
            updated_at=model.updated_at,
            teacher=TeacherModelMapper.to_domain(model.teacher)
        )
