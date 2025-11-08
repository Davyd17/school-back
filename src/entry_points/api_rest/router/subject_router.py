from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from app.dependencies.subject_provider import provide_find_all_subjects
from application.usecase.subject.find_all_subjects import FindAllSubjects
from entry_points.api_rest.response.subject.subject_response import SubjectResponse
from entry_points.api_rest.response.subject.subject_response_mapper import SubjectResponseMapper

router = APIRouter(prefix="/subject", tags=["subject"])

@router.get("/", response_model=List[SubjectResponse])
def read_subjects(usecase: FindAllSubjects
                    = Depends(provide_find_all_subjects)):

    subjects = usecase.execute()

    return[SubjectResponseMapper.from_domain(subject) for subject in subjects]