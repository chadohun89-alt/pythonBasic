# attendance_service.py

from fastapi import HTTPException

from models.attendance import Attendance
from models.student import Student
from schemas.attendance_schema import AttendanceCreate, AttendanceResponse

def create_attend_service( attendance, db ):
    attendanceData = [attendance.attend, attendance.late,
                      attendance.absent, attendance.early_leave ]
    attabs = ["attend", "late", "absent", "early_leave"]
    
    # 학생 존재 여부
    student = db.query(Student)\
        .filter(Student.id == attendance.student_id)\
            .first()
    
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="학생 정보를 찾을 수 없습니다."

        )
    
    new_attendance = Attendance(
        student_id = attendance.student_id,
        attend = attendance.attend,
        late = attendance.late,
        absent = attendance.absent,
        early_leave = attendance.early_leave
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

def get_attendance_list( db ):
    attendance_list = db.query(Attendance,Student)\
    .join(Student, Attendance.student_id == Student.id)\
    .all()

    

    result = []
    for atd, std in attendance_list:
        total_count = (atd.attend + atd.late +
                    atd.absent + atd.early_leave)
        attendance_rate = round((atd.attend/total_count) * 100, 1)

        result.append( AttendanceResponse(
            id = atd.id,
            student_id=std.id,
            student_name=std.name,
            attend=atd.attend,
            late=atd.late,
            absent=atd.absent,
            early_leave=atd.early_leave,
            total_count=total_count,
            attendance_rate=attendance_rate,
        ))
    return result

    '''
    id:int
    student_id:int
    student_name:str
    attend:int
    late:int
    absent:int
    early_leave:int
    total_count:int
    attendance_rate:float

    '''
