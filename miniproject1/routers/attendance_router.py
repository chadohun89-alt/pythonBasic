# attendance_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db

from schemas.attendance_schema import (AttendanceCreate, AttendanceResponse)
from service.attendance_service import create_attend_service, get_attendance_list

router = APIRouter()

# 출석률 등록
@router.post("/attend")
def create_attend(attendance:AttendanceCreate, db:Session= Depends(get_db)):
    return create_attend_service(attendance, db)

# 출석률 조회
@router.get("/attend")
def get_attend(db:Session=Depends(get_db)):
    return get_attendance_list(db)