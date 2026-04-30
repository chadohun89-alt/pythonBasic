'''
db_study3.py에서 연결한 MySQL의 item 테이블을 사용하세요.

해야 할 것:

item 테이블 전체를 가격(price) 높은 순서로 조회해서 출력
category가 '총'인 아이템만 조회해서 이름과 가격만 출력
예상 출력 (예시):


-- 가격 높은 순 --
('M4A1 카빈', 1500000, ...)
('K2 소총', 1200000, ...)
...

-- 총 카테고리 --
M4A1 카빈 : 1,500,000원
K2 소총 : 1,200,000원
...
힌트: SQL 정렬은 ORDER BY 컬럼명 DESC

'''

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="ckehgjs",
    password="1234",
    database="ckehgjs",
    charset="utf8"
)

cur = conn.cursor()

cur.execute("select item_name, item_price from item order by item_price desc")

container = cur.fetchall()

print("-- 가격 높은 순 --")
for item in container:
    print(item)


cur.execute("select item_name, item_price from item where category = '총' order by item_price desc")
print()
print("-- 총 카테고리 --")
for item in cur:
    print(item)


