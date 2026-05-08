# pandas_sql.py

from sqlalchemy import create_engine
import pandas as pd


# create_engine("mysql+pymysql://계정명:비번@주소:3306/DB명")
eng = create_engine(
    "mysql+pymysql://ckehgjs:1234@localhost:3306/ckehgjs"
)


conn = eng.connect()
print("연결 성공")
conn.close()
print("연결 닫기")

 # 연결 닫기 한 건 뭐지?

query = "select * from item"
df = pd.read_sql(query, eng)
print(df)

# Database -> DataFrame -> 파일 저장
# 위 과정을 사용하는 경우는 보고서 작성이나
# 다른 시스템에 데이터를 전달하기 위함

# 회사에서는
# 데이터 수집( 파일, 스크랩핑 emd) -> DataFrame -> Database
# 위 과정으로 사용하는 게 일반적이다.

# 카테고리별 수량
print(df['category'].value_counts())

# status 컬럼에서 sale 개수와 soldout 개수는?
print(df['status'].value_counts())

# status가 sale인 총은 전체 몇개 인가?
gun = df[df['category'] == '총']
gun_cnt = gun['status'].value_counts()
print("판매중인 총의 개수 : ", gun_cnt['sale'], "개")

# 문제 3. 미사일 중에서 수량(item_qa) 이 10개 이상인
# 미사일의 이름을 출력하세요.

# misail = df['category'] == '미사일'
# misail['item_qa' >= 10]

# misail = df[df['category'] == '미사일']
# misail_name = misail.loc[misail['item_qa'] >= 10, ['item_name']]
# print(misail_name)

print("문제 3 : 미사일 이름")
mi = df[
    (df['category'] == '미사일') &
    (df['item_qa']>=10)
]
print(mi['item_name'].to_string(index=False))