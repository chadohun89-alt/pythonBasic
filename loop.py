# # loop.py

print("숫자 : 1")
print("숫자 : 2")
print("숫자 : 3")
print("숫자 : 4")
print("숫자 : 5")
print()
# # 5번 반복하는 반복문
for i in range(5,0,-1):
    print("숫자 : " + str(i))

print("===========================")

for ch in "hello":
    print(ch)

for name in ["차도헌","박지연","이성찬","김진숙","이동렬","김현규"]:
    if name.startswith("이"):
        print(name)

# #문제1. 1부터 10까지의 총합을 구하세요. 반복문을 사용해서

total = 0
for i in range(1,11):
    total += i

print("총합: " + str(total))


# #문제 2. ["15,000", "13,000", "8,700", "9,000", "25,000"]
# # 배열에 출금 금액들이 저장되어있다.
# # 만원 이상 금액들에 대해 출력하세요

# # 반복문으로 하나씩 뽑아서 replace + int함수로 가공
# # 조건문으로 만원 이상일 경우 출력
# # 출력 형태는 금액: 000원

money = ["15,000", "13,000", "8,700", "9,000", "25,000"]

for m in money:
    m = int(m.replace(",",""))
    if m >= 10000:
        print(m)

for i in range(len(money)):
    print("금액:", i+1, money[i])

for i, v in enumerate(money):
    print(i, v)

print()

# 문제 3. [89, 56, 78, 92, 61, 96, 83, 74]
# 203호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요

array = [89, 56, 78, 92, 61, 96, 83, 74]
total = 0
avg = 0
count = 0

for i, v in enumerate(array):
    # v = int(v)
    total += v
    count = i+1

avg = total / count

print("총합:", total)
print("평균:", avg)

print()
# 반복문 while

# while 조건:
#     실행코드

# while문은 조건식이 참인 경우에 동작 하기 때문에
# 쉽게 무한루프에 들어갈 수 있다.
# 하여 while문 사용시 중단시킬 수 있는 break를 같이 사용하는 게 좋다.

num = 5
while num > 2:
    print("2보다 크다")
    break

while True:
    num += 1
    if num == 7: continue # 건너뛰기
    print(num)
    if num == 10: break

print("==================")

while True:
    cmd = input("명령어 입력 : ").strip().lower()
    if cmd == "history":
        print("모든 기록 출력")
    elif cmd == "mkdir":
        print("새로운 폴더 만들기")
    elif cmd == "remove":
        print("파일 삭제")
    elif cmd == "exit":
        print("종료")
        break
    else:
        print("존재하지 않는 명령어입니다.")

#파이썬 랜덤 사용
import random

# num = random.randint(1,10)
# print(num)
# 동전 앞면 뒷면 맞추기 게임 만들기

# while True:
#     again = input("시도/그만: ")
#     number = random.randint(1,2)
#     if again == "시도":
#         if number == 1:
#             print("앞면")
#         if number == 2:
#             print("뒷면")
#     if again == "그만":
#         print("종료")
#         break


# coin = random.randint(1,2)
# user = int(input("1. 앞면, 2. 뒷면 :"))
# if coin == user:
#     print("정답")
# else:
#     print("땡!!")

# n = random.randrange(1,10) # 1~9

# game = ["가위", "바위", "보"]
# n = random.choice(game)

# print(n)


# 가위바위보 게임 5판 진행.
# 5번째 게임이 끝나면 몇승 몇패 몇무인지 출력

# for문 사용
# count123 변수로 승리, 무승부, 패배 카운팅

# game = ["가위", "바위", "보"]

# win = 0
# draw = 0
# lose = 0


# for i in range(5):
#     ho = random.choice(game)
#     user = input("가위 / 바위 / 보 중에 골라서 내:")
#     if ho == user:
#         print("무승부")
#         draw += 1
#     elif (ho == "가위" and user == "바위") or (ho == "바위" and user == "보") or (ho == "보" and user == "가위"):
#         print("승리")
#         win += 1
#     elif (ho == "가위" and user == "보") or (ho == "바위" and user == "가위") or (ho == "보" and user == "바위"):
#         print("패배")
#         lose += 1
#     else:
#         print("똑바로 안 낼래?")

# print("승리:", win, "무승부:", draw, "패배:", lose)

game = ["가위", "바위", "보"]

win = lose = draw = 0
for i in range(5):

    com = random.choice(game)
    user = input("가위 바위 보 : ").strip()

    print("컴퓨터 : ", com, "나 : ", user)
    # 승 패 무 판단
    # game.index("가위")
    # 사전적 순서 비교 방법은 비교연산자
    cidx = game.index(com)
    uidx = game.index(user)

    comp = cidx - uidx #유저와 컴의 가위바위보값 비교
    # 가위-0, 바위-1, 보-2 -> 유저가 0, 컴이 1이라면 컴의 승
    # 즉 comp에 1이 있다면 컴의 승

    if com == user:
        print("비김")
        draw += 1
    elif comp == -1 or comp == 2:
        print("나의 승")
        win += 1
    else:
        print("나의 패")
        lose += 1

print("승/무/패:", win, draw, lose)


    