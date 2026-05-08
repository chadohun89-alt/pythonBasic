# 새폴더 만들기 - pandas_study
# 새 파일 - pandas_study1.py

# pandas는 데이터 분석용 라이브러리
# numpy 숫자배열 계산 pandas는 데이터를 표형식으로 관리 하여 분석용이
# numpy[ [ 1, 2 ] , [ 3, 4 ] ]
# pandas
#  이름   점수
# 이순신   89
# 박문수   67

import pandas as pd



# 2차원 데이터 만들기
df = pd.DataFrame(
    {
        "name":["이순신","박문수", "이성계","정약용","문익점","한석봉","계백"],
        "score":[89,67,80,91,67,99,57],
        "gender":["남","여","남","남","여","여","남"]
    }
)
print(df)

# 1. 집계
# 1-1 데이터 합계
print(df['score'].sum())

# 1-2 특정 컬럼 안에 데이터가 몇개 있는지
print(df['score'].value_counts())

# 2. 행 단위 자르기
print("\n 데이터 프레임 - 특정 행 출력하기 \n")
print(df.head(3))
print(df.tail(4))
# head와 tail 함수는 파일 데이터 불러오기 했을 때 확인용으로 많이 사용
# 로그 파일을 확인할 때 최근 문제를 보려면 tail 함수로 빠르게 확인 가능

# 3. 데이터 정보 확인
print("\n 데이터프레임의 데이터 정보 확인 \n")
print( df.info() )
print( df.describe() )
# 숫자 데이터의 평균, 최솟값, 최댓값, 분포, 데이터 갯수, 표준편차

# 4. 조건검색
print("\n 데이터프레임 조건 검색 \n")
# 4-1
res_df = df[df['score'] >= 80]
print(res_df)

# 4-2 포함
name_df = df[df['name'].str.contains("이")]
print(name_df)
# 문자열 완전일치는 == 연산자

# 4-3 논리연산자
res_df = df[  (df['score'] >= 80) & (df['score'] <= 90)  ]
print(res_df)

# 4-4 여러개 검색에는 isin 함수 사용
res_df = df[ df['name'].isin(['이순신','한석봉'])]
print("isin")
print(res_df)

# 4-5 범위 검색 between
res_df = df[ df['score'].between(80,90)]
print(res_df)


res_df = df.query('score >= 80 and score <= 90')
print(res_df)

# 4-6 특정 컬럼(필드)만 가져오기
res_df = df.loc[df['score'] >= 80, ['name']]
print(res_df)

# 5. 정렬
df.sort_values("score", ascending=False)
print(df)



# 6. 그룹화
res_df = df.groupby('gender')['score'].sum()
print(res_df)

'''
groupby의 집계 함수들

컬럼이 여러개라면 함수 앞에 집계할 컬럼 넣어야 된다.

1. sum() - 총합 df.groupby('gender').sum()   
   mean() - 평균 df.groupby('gender').mean() 
2. count() - 개수 df.groupby('gender').count()
   size() - 행 개수 df.groupby('gender').size()
    count와 size의 결과가 같은 경우가 많은데 차이는
    count는 NaN 제외하고, 개수파악, size는 NaN 포함 개수 세기
3. std() - 표준편차 df.groupby('gender').std()
4. min()
   max()
   median() - 중앙갑 df.groupby('gender').median()
5. var() - 분산 df.groupby('gender').var()
6. first() - 첫번째값 df.groupby('gender').first()
    last()
7. agg() - 여러개의 집계함수 사용 df.groupby('gender').agg(['sum', 'mean])
    
    컬럼별로 다른 집계함수 사용
    df.groupby('gender').agg({
     "score" : "sum"
     "name" : "count"   
    })
    
'''


# s = pd.Series([89,67])
# print(s)