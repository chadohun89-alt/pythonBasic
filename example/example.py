# 문제1. json 읽기

import json

data = json.loads('''
{
    "store": "무기상점",
    "items": [
        {"name": "K2 소총", "price": 1200000, "category": "총"},
        {"name": "MP5", "price": 1100000, "category": "총"},
        {"name": "K-1 전투도끼", "price": 350000, "category": "도끼"},
        {"name": "전투나이프", "price": 180000, "category": "도끼"},
        {"name": "M4A1", "price": 1500000, "category": "총"}
    ]
}
''')

# 상점 이름
store_name = data["store"]
print(store_name)

# 아이템 개수
items_qa = len(data["items"])
print("아이템 개수 : ", items_qa)

# 카테고리가 총인 아이템
gun = list()

for item in data["items"]:
    if item["category"] == "총":
        gun.append(item["name"])

print(gun)

# 가장 비싼 아이템(이름과 가격)

max_price = 0
max_name ="시작"

for item in data["items"]:
    if int(item["price"]) > max_price:
        max_price = int(item["price"])
        max_name = item["name"]

print(f"가장 비싼 아이템 :  {max_name} / {max_price:,}원")

print()
print("문제2")
print()
# 문제2. 예외 처리
def calc(a, b):
    return a / b

numbers = [10, 0, 5, "삼", 2]


for n in numbers:
    try:
        result = calc(100, n)
        print(f"100 / {n} = {result}")
    except ZeroDivisionError as z:
        print("0으로는 나눌 수 없습니다.")
    except TypeError as t:
        print("숫자가 아닙니다.") 

