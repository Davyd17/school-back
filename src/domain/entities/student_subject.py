from dataclasses import dataclass
from decimal import Decimal

@dataclass
class StudentSubject:
    student_id: int
    subject_id: int
    average: Decimal = Decimal("0.00")