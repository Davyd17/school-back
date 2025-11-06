from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from domain.usecase.subject.subject_find_all_usecase import SubjectFindAllUseCase
from infraestructure.entry_points.api_rest.provider.subject_provider import provide_subject_find_all_usecase
from infraestructure.entry_points.api_rest.response.subject.subject_response import SubjectResponse
from infraestructure.entry_points.api_rest.response.subject.subject_response_mapper import SubjectResponseMapper

router = APIRouter(prefix="/subject", tags=["subject"])

@router.get("/", response_model=List[SubjectResponse])
def read_subjects(usecase: SubjectFindAllUseCase
                    = Depends(provide_subject_find_all_usecase)):

    subjects = usecase.execute()

    return[SubjectResponseMapper.from_domain(subject) for subject in subjects]