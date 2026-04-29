# tashu.py

# 대전 광역시 자전거 타슈의 위치 현황 파일을 불러오기
# 타슈 자전거 정거장 위치 찾기 만들기
# 동, 이름 또는 현재 위치(건물, 지명 등등) 입력받기
# 검색어가 포함되어 있는 정거장 이름 또는 주소에서 찾기

# 조회한 정체 정거장을 출력하는데 중복없어야 되고
# 정거장명 기준 내림차순으로 정렬 하기

# 요구사항 정리 : 
# 1. 파일 불러오기
#   open() 
# 2. 키워드 입력받기(동, 이름, 현재위치)
#   input().strip()
# 3. 검색어가 포함되어 있는 정거장 이름 또는 주소 에서 찾기
#   for문. 2중 반복문. 1번 : 리스트에서 딕셔너리 꺼내기. 2번 딕셔너리에서 키 밸류별로 꺼내기
# 4. 중복 없을 것
#   set 사용
# 5. 정거장명 기준 내림차순 정렬
#   sorted() 사용


import csv

# station_lits = list()

# with open("file/타슈.csv", "r") as f:
#     data = csv.DictReader(f)
#     header = next(data) # 대전축제 csv의 필드명 header에 리스트로 저장


tashu_list = list() # csv 데이터 저장할 리스트

with open("file/타슈.csv", "r") as f:
    data = csv.reader(f)
    header = next(data) # 대전축제 csv의 필드명 header에 리스트로 저장

    for row in data:
        temp_dic = dict() # 빈 딕셔너리 - 하나의 타슈장소에 대하여 저장
        for i, v in enumerate(row):
            temp_dic[header[i]] = v
        tashu_list.append(temp_dic)

# 타슈 검색하기
# 입력한 키워드가 포함 되어있는 장소를 찾는다.
# 검색에 제외할 키 - 문의전화, 주최, 주관 > 삭제

keyword = input("타슈 검색 : ").strip() # 공백 제거(좌우)

result = set() # 검색 결과 정거장이 저장될 set

for row in tashu_list:
    for k, v in row.items():
        if k == header[0] or k in header[3:11]:
            continue
        if keyword in v:
            result.add((row["정거장"]))


result2 = sorted(result, reverse= True)
for row in result2:
    print(row)