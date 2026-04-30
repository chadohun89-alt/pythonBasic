# 문제3.

# 요구사항
# 테이블 만들기 (student)
# 데이터 넣기
# 조회하기

'''
1. practice.db 파일로 SQLite 연결
2. students 테이블 생성
3. 아래 데이터 3개 이상 삽입
    - 김유신 / 85
    - 강감찬 / 92
    - 이순신 / 78
4. 전체 조회해서 출력
5. score가 80점 이상인 학생만 조회해서 출력

'''

import sqlite3

conn = sqlite3.connect("practice.db")
cur = conn.cursor()

# cur.execute('''
#     create table students(
#         id integer primary key autoincrement,
#         name text,
#         score integer
        
#     )
# ''')

data = (("김유신", 85), ("강감찬", 92), ("이순신", 78))

cur.executemany("insert into students(name, score) values(?,?)",
            data)
conn.commit()

cur.execute("select * from students")
mans = cur.fetchall()

print("-- 전체 --")
for man in mans:
    print(man)

print()
print("-- 80점 이상 --")
for man in mans:
    if man[2] >= 80:
        print(man)