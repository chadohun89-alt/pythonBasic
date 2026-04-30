# db_study1.py

# SqlLite = 설치 안함, 파일 하나로 동작하는 내장형 데이터베이스
# MYsql 같은 데이터베이스는 프로그램 <-> DB서버 <-> 데이터
# SqlLite는 프로그램 <-> DB파일

'''
    
    INTEGER -   숫자(정수)
    REAL    -   실수
    TEXT    -   문자열
    BLOB    -   바이너리
    NULL    -   값 없음

'''


import sqlite3

conn = sqlite3.connect("test.db") # 파일 생성 후 연결 / 이미 있는 파일은?
cur = conn.cursor() # 커러 생성

# cur.execute("""
#     create table info(
#         id integer primary key autoincrement,
#         name text,
#         age integer
#     )
# """)

# cur.execute("insert into info (name, age) values (?, ?)",
#             ("김유신", 34))

# conn.commit() # 저장


cur.execute("select * from info")

rows = cur.fetchall() # f.read()
# 테이블에서 한 줄씩 읽기 - fetchone()
# n개 가져오기 - fetchmany(n)


for row in rows:
    print(row)