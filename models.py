
from pydantic import BaseModel
from typing import List

class StudentGrade(BaseModel):
    name: str
    grade: float

class AnalysisRequest(BaseModel):
    students: List[StudentGrade]
    prompt: str
