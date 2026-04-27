#function1.py

# 자바 : 제어자 반환타입 메서드이름 ( 매개변수 )

# 파이썬 함수 : def 함수이름(함수이름):

def hi():
    print("안녕")

# 함수 실행 - 호출
# 함수 이름() - () 소괄호에 매개변수가 있다면 넣어주기
hi()

def intro(name : str):
    print(name,"님 로그인 하셨습니다.")

name = "김유신"
if type(name) == str: # isinstance(name, str)
    intro(name)



intro("하늘소")
intro("감기약")
intro(1000)


def dataInput(a,b,c):
    print (a + b + c)

dataInput(1, 20, 30)

# 함수를 만들 때(정의) 어떤 기능을 가진 함수를 만들 것인가?
# 해당 기능이 작동되기 위해서 필요한 것이 무엇인가
# 필요한 것들이 함수 안에서 만들 수 있는 것인가 아니면 외부에서 받아야 하는 것인가


# 함수의 반환 값 return - 함수가 호출된 위치로 값을 돌려보내는 작업

def add(num1, num2):
    return "계산 결과", num1 + num2

comment, res= add( 10,20 )
print(comment,":", res)

# 변수의 범위 - 지역변수, 전역변수
number = 1000
def totalPrice( price ):
    total = 0
    for money in price:
        total += money
    global number
    number = total  # 전역변수의 수정은 안 된다. global을 붙여야 수정가능


totalPrice([1,2,3,4,5])
print(number)


# 문제1. 간단한 함수 만들기
# 사각형의 너비와 높이를 받아서 넓이를 출력하는 함수를 만들어 호출해보세요.

def square (width, height):
    res = width*height
    print(f"사각형 넓이 : {res}㎠")

square(20,5)

# 문제2. 아래 코드를 보고 함수를 만드세요
# 로그인 체크 함수 만들기


# def login_check(id, pw):
#     if id == "admin" and pw == "1234":
#         return True
#     else: return False

# id = input("아이디를 입력하세요 : ").strip()
# pw = input("비밀번호를 입력하세요 : ").strip()

# if login_check(id,pw):
#     print("로그인 성공 하였습니다.")
# else:
#     print("아이디 또는 비밀번호를 잘못 입력했습니다.")


# 문제3. 상품의 재고를 확인하여 재고 충분, 재고 부족, 품절이라고 출력 할 수 있는 함수 만들기
# 재고 부족 기준은 현재 재고량이 8이하인 경우
# 위 코드를 print( 함수 호출 ) 이렇게 실행하면 동작할 수 있게 함수 만드시오

# item_stock = 12

# if item_stock > 8:
#     print("재고 충분")
# elif item_stock <= 8:
#     print("재고 부족")
# else:
#     print("품절")

item_stock = 12

def stock_check(stock):
    
    if stock > 8:
        print("재고 충분")
    elif stock > 0:
        print("재고 부족")
    else:
        print("품절")

print(stock_check(item_stock))

# 문제4. 회원가입을 한다. 아이디 중복체크 함수를 만드세요.

id_list = ["kim", "lee","sky","gold","war123","qwer12","eeee14"]

#id_list는 현재 가입된 회원들의 아이디만 저장된 리스트이다.
# 아이디 중복체크 함수를 통해 사용가능, 불가능을 출력하세요.

# def id_check(list):
#     input_id = input("아이디를 입력 : ").strip()
#     checked = False
#     for id in list:
#         if id == input_id:
#             checked = True
#     if checked:
#         print("사용 불가능")
#     else:
#         print("사용 SSAP가능!")

# id_check(id_list)

def id_check(id):
    global id_list
    if id in id_list:
            return "사용 불가능"
    else:
            return "사용 가능"
    
print(id_check("park"))


