from application.gateway.repository.model.student_subject import StudentSubjectRepository


class FindAllStudentSubject:
    def __init__(self, repository: StudentSubjectRepository):
        self.repository__ = repository

    def student_subject_find_all_reposity(self):
        return self.repository__.get_all()