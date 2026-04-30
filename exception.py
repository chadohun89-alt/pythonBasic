# exception.py

# print("오류??")

# print( 2 + 2)

# try:
#     print( 10 / 0)
# except:
#     print("오류인가?")

# try:
#     num = int(input("숫자 입력 : "))
#     print(num)
# except Exception as e:
#     print(e)

# try:
#     # 오류가 예상되거나 사용자와 밀접한 코드
# except FileNotFoundError:

# except KeyError:



# try:
#     f = open("a.text", "r")
# except FileNotFoundError:
#     print("존재 하지 않는 파일입니다.")

# finally:
#     f.close()
#     print("오류가 있어도 없어도 실행")

try:
    with open("a.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("존재하지 않는 파일입니다.")
else:
    print("오류가 없을 때만 실행")

# 숫자 입력을 잘 할 때까지 계속 입력 받기


def check_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상어야 한다")
    
while True:
    try:
        num = int(input("나이 : "))
        check_age(num)
        break

    except ValueError as e:
        print(e)
    except:
        print("다시 입력하세요")

'''

    1. ValueError - 값이 잘못된 경우
    2. TypeError - 타입이 맞지 않은 경우

    3. ZeroDivisionError - 0으로 나눔

    4. IndexError - 인덱스 범위 초과
    5. KeyError - 딕셔너리 키 없는 경우
    
    6. NameError - 변수 없는 경우
    7. ArrtibuteError - 속성/메서드 없는 경우
    
    8. FileNotFoundError - 파일 없는 경우
    
'''