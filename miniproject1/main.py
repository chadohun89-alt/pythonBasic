# 폴더 miniproject1 (opencv 빼고 / 2는 포함해서)
# 새파일 - main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import Base, engine

# 모델과 스키마가 main에 왜 필요하지?
from models import student, score, attendance
from schemas import student_schema, score_schema, attendance_schema

from routers import student_router, score_router, attendance_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router.router)
app.include_router(score_router.router)
app.include_router(attendance_router.router)
