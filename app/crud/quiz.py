from typing import List
from sqlalchemy import desc, select

from app.core.db import AsyncSessionLocal
from app.models.quiz import Quiz
from app.schemas.quiz import QuizCreate


async def create_quiz_db(new_quiz: QuizCreate) -> Quiz:
    new_quiz_data = new_quiz.dict()
    db_quiz = Quiz(**new_quiz_data)

    async with AsyncSessionLocal() as session:
        session.add(db_quiz)

        await session.commit()
        await session.refresh(db_quiz)
    return db_quiz


async def get_last_quiz() -> Quiz:
    async with AsyncSessionLocal() as session:
        latest_quiz = await session.execute(
            select(Quiz).order_by(Quiz.id.desc()).limit(1)
        )
    return latest_quiz.scalar()


async def get_quiz_by_question_id(quiz_id: int) -> Quiz:
    async with AsyncSessionLocal() as session:
        quiz = await session.execute(
            select(Quiz).where(Quiz.question_id == quiz_id)
        )
        quiz = quiz.scalar()
    return quiz
