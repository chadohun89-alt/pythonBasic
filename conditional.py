#conditional.py
# if( i > 5) { # 자바, 자바스크립트 방법

# }else{

# }
# if 조건식:
#   실행할 코드

num = 3
if num > 5:
    print("크다")
    print("10이 크다")
elif num < 5:
    print("작다")
    print("5보다 작다")

# 변수 apple의 값이 10이상이라면 "1봉지 8000원"라고 출력
# apple의 값이 10미만이라면 "개당 2000원" 출력

apple = 8
if apple >=10:
    print("1봉지 8000천원")
else:
    print("개당 2000원")

# switch(res){
#     case 1:
#         실행코드
#     case 2:
#         실행코드
# }

res = 2
match res:
    case 1 | 4:
        print("숫자 1 또는 4이다")
    case 2:
        print("숫자 2이다.")
    case int():
        print("정수 이다")
    case 3.5:
        print("숫자 3.5이다.")
    
# like 좋아요 변수의 값이 100이상이면 "spot 등록" 출력
# 좋아요 변수의 값이 10이하라면 "관심 spot" 출력

# like = int(input("좋아요 갯수는 : "))
# print(like)
# if like >= 100:
#     print("spot 등록")
# elif like <= 10:
#     print("관심 spot")

# 아이디와 비밀번호 입력 받아 일치하면 로그인성공, 불일치면
# 아이디 또는 비밀번호가 잘못되었습니다. 출력
# 아이디는 진섭, 비밀번호는 babo 

# id = input("아이디 입력 : ")
# pw = input("비번 입력 : ")

# if id == '진섭' and pw == 'babo':
#     print("로그인 성공")
# else:
#     print("아이디 또는 비밀번호가 잘못되었습니다.")

# 파이썬에서 문자열 포함여부 확인하는 방법

word = "나는 김진섭입니다."
if '김진섭' in word:
    print("있다")
else:
    print("없다")

word = "나는 진섭이가 짝꿍일 때 별로였다."

# word 안에 동렬 이름이 없다라는 것을 출력하세요.

if '동렬' not in word:
    print("동렬 없다~!")

#startswith() 함수 시작 문자열 비교
word = "차도헌님께서 입장하셨습니다."

if word.startswith('이창호'):
    print("신원 확인")
else:
    print("이창호님이 아닙니다.")

# 대소문자 변환
word = "i like banana"
print( word.upper()) # 대문자
print( word.lower()) # 소문자
print( word.title()) # 대문자 - 단어의 첫글자만

# 공백제거 - 개발 시 필요필수 (이거 때문에 오류나면 골치아픔)
word = " banana "
print(word) # 공백제거 없이
print(word.strip()) # 양쪽 공백제거
print(word.lstrip()) # 왼쪽 공백제거
print(word.rstrip()) # 오른쪽 공백제거

# 찾기
word= "찬용이는 진섭이보다 지금이 좋다고 한다."
print(word.find("진섭")) # 있다면 위치 반환(인덱스) 없으면 -1
print(word.index("동렬")) # 인덱스 반환, 없으면 에러
