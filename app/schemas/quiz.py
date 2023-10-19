from datetime import datetime

from pydantic import BaseModel


class QuizBase(BaseModel):
    question: str
    answer: str

    class Config:
        orm_mode = True


class QuizCreate(QuizBase):
    question_id: int
    airdate: datetime
