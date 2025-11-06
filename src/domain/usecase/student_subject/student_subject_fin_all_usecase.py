from domain.gateway.student_subject_repository_gateway import StudentSubjectRepositoryGateway


class StudentSubjectFindAllUseCase:
    def __init__(self, repository: StudentSubjectRepositoryGateway):
        self.repository__ = repository

    def student_subject_find_all_reposity(self):
        return self.repository__.get_all()