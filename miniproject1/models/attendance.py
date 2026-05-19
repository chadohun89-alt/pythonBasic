# attendance.py

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from database.db import Base

class Attendance(Base):
    __tablename__="attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    attend = Column(Integer)
    late = Column(Integer)
    absent = Column(Integer)
    early_leave = Column(Integer)

'''
attendance
	id	
    student_id	
    attend	
    late	
    absent	
    early_leave


'''