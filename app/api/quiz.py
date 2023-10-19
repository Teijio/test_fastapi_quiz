import json

import requests
from fastapi import APIRouter, HTTPException

from app.crud.quiz import (
    create_quiz_db,
    get_last_quiz,
    get_quiz_by_question_id,
)
from app.schemas.quiz import QuizBase, QuizCreate

router = APIRouter()

URL = "https://jservice.io/api/random?count="
ONE_QUIZ = 1


def fetch_quiz_data(questions_num: int, URL: str) -> dict:
    response = requests.get(f"{URL}{questions_num}")
    if response.status_code != 200:
        raise HTTPException(
            status_code=500, detail="Failed to fetch quiz data"
        )
    return json.loads(response.content)


async def get_unique_quiz():
    while True:
        new_quiz = fetch_quiz_data(ONE_QUIZ, URL)
        quiz_dict = {
            "question_id": new_quiz["id"],
            "question": new_quiz["question"],
            "answer": new_quiz["answer"],
            "airdate": new_quiz["airdate"],
        }
        if not await get_quiz_by_question_id(quiz_dict["question_id"]):
            return quiz_dict


def swap_answers(quiz_dict, previous_answer):
    curr_answer = quiz_dict["answer"]
    quiz_dict["answer"] = previous_answer
    return quiz_dict, curr_answer


@router.post("/{questions_num}", response_model=list[QuizBase])
async def create_new_quiz(questions_num: int):
    quizzes_data = fetch_quiz_data(questions_num, URL)
    quizzes_list = []
    quiz_previous_answer = []

    if last_quiz := await get_last_quiz():
        quiz_previous_answer = last_quiz.answer

    for quiz in quizzes_data:
        quiz = {
            "question_id": quiz["id"],
            "question": quiz["question"],
            "answer": quiz["answer"],
            "airdate": quiz["airdate"],
        }

        quiz_in_base = await get_quiz_by_question_id(quiz["question_id"])

        if quiz_in_base:
            quiz = await get_unique_quiz()

        quiz_into_schema = QuizCreate(**quiz)
        await create_quiz_db(quiz_into_schema)

        quiz, quiz_previous_answer = swap_answers(quiz, quiz_previous_answer)
        quizzes_list.append(quiz)

    return quizzes_list