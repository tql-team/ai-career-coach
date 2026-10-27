# SPDX-License-Identifier: MIT
from pydantic import BaseModel
from typing import List


class RegisterInput(BaseModel):
    name: str
    email: str
    password: str


class LoginInput(BaseModel):
    email: str
    password: str


class JobCreateAI(BaseModel):
    title: str
    description: str


class CVInput(BaseModel):
    name: str
    email: str
    cv_text: str
    free_time_json: str


class StarAnswerInput(BaseModel):
    student_answer: str


class FeedbackInput(BaseModel):
    profile_id: int | str
    job_id: int | None = None
    is_match: bool


class ScheduleItem(BaseModel):
    id: int
    exactDate: str
    dayOfWeek: str
    timeStart: str
    timeEnd: str


class StudyPlanRequest(BaseModel):
    profile_id: str
    role_id: str | None = "1"
    schedules: List[ScheduleItem] = []
    gaps: List[str] = []
    jd_text: str | None = ""
    target_role: str | None = ""


class UpdateScheduleRequest(BaseModel):
    profile_id: str | int
    schedules: List[ScheduleItem]


class TaskCompleteInput(BaseModel):
    task_id: int


class InterviewRequest(BaseModel):
    profile_id: str | None = None
    persona: str | None = "tech_lead"
    level: str | None = "mid"
    language: str | None = "vi"
    analysis_context: dict | None = None
    random_nonce: int | None = None


class AnswerSubmitRequest(BaseModel):
    profile_id: int | str = 1
    question_text: str
    student_answer: str
    language: str | None = "vi"
    job_id: int | None = None
    question_category: str | None = None
