from sqlalchemy import Column, DateTime, Integer, String, Text

from app.core.db import Base


class Quiz(Base):
    question_id = Column(Integer)
    question = Column(Text)
    answer = Column(String)
    airdate = Column(DateTime)
