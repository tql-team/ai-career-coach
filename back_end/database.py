# SPDX-License-Identifier: MIT
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://admin:secretpassword123@localhost:5433/career_coach"
)
_connect_args = (
    {"connect_timeout": 3}
    if SQLALCHEMY_DATABASE_URL.startswith("postgresql")
    else {"check_same_thread": False}
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    connect_args=_connect_args
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine
)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
