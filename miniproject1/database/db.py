# database/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://ckehgjs:1234@localhost:3306/ckehgjs"

# 데이터베이스 연결 - echo는 실행하는 sql 출력(개발 시 또는 로그 기록용)
engine = create_engine(DB_URL, echo=True)

# DB 쿼리문 실행시킬 객체
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM 부모 같은?
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
1. /students 요청이 들어옴
2. FastAPI가 get_db() 실행
3. SessionLocal()로 DB 세션 생성
4. yield db로 라우터 함수에 세션 전달
5. 라우터에서 db.query(), db.add() 사용
6. 요청 처리 끝
7. finally로 돌아와서 db.close() 실행

'''