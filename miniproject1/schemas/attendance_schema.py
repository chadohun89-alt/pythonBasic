# pttendance_schema.py

from pydantic import BaseModel
from datetime import datetime

class AttendanceCreate(BaseModel):
    student_id:int
    attend:int
    late:int
    absent:int
    early_leave:int

class AttendanceResponse(BaseModel):
    id:int
    student_id:int
    student_name:str
    attend:int
    late:int
    absent:int
    early_leave:int
    total_count:int
    attendance_rate:float

    class Config:
        from_attributes=True


