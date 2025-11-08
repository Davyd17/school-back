from domain.entities.student_subject import StudentSubject
from infraestructure.repository.SQLModel.model.student_subject_model import StudentSubjectModel


class StudentSubjectModelMapper:

    @staticmethod
    def from_domain(domain: StudentSubject) -> StudentSubjectModel:

        return StudentSubjectModel(
            student_id=domain.student_id,
            subject_id=domain.subject_id,
            average=domain.average
        )

    @staticmethod
    def to_domain(model: StudentSubjectModel) -> StudentSubject:

        return StudentSubject(
            student_id=model.student_id,
            subject_id=model.subject_id,
            average=model.average
        )