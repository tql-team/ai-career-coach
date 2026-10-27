# SPDX-License-Identifier: MIT
from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey
from database import Base


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    skills_json = Column(Text)
    interests_json = Column(Text)
    experience_text = Column(Text)
    free_time_json = Column(Text)


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    requirements_json = Column(Text)


class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    total_score = Column(Float)
    gaps_json = Column(Text)
    reasons_json = Column(Text)


class StudyTask(Base):
    __tablename__ = "study_tasks"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    title = Column(String)
    duration_minutes = Column(Integer)
    scheduled_day = Column(String)
    unlock_time = Column(String)
    deadline_time = Column(String)
    status = Column(String, default="locked")


class StreakAndReport(Base):
    __tablename__ = "streaks_and_reports"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    seed_stage = Column(String, default="Hạt giống")
    current_xp = Column(Integer, default=0)
    weekly_xp = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    last_study_date = Column(String, default="")
    last_watered_date = Column(String, default="")
    last_leave_date = Column(String, default="")
    recovery_mode = Column(Boolean, default=False)
    total_roadmap_minutes = Column(Integer, default=0)
    completed_roadmap_minutes = Column(Integer, default=0)
    planned_tasks_weekly = Column(Integer, default=0)
    completed_tasks_weekly = Column(Integer, default=0)
    discipline_score = Column(Float, default=0.0)


class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    is_match = Column(Boolean)


class Interview(Base):
    __tablename__ = "interviews"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    questions_json = Column(Text)
    student_answer_text = Column(Text)
    evaluation_json = Column(Text)
