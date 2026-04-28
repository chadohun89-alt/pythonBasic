# file -> file_test.py

# 파일 입출력 - 프로그램에서 생성된 데이터들은 프로그램 종료 시
# 메모리에서 사라진다. 필요한 데이터들을 남겨두기 위해서는 파일로 저장을
# 해야한다. 파일 입출력은 데이터를 저장하고 불러오는 방법이다.

# 파일 쓰기 - 저장, 파일 읽기 - 불러오기

# open("파일명", "모드") # 모드 - r : 읽기, w : 쓰기(덮어쓰기), a : 추가

# f = open("file/test1.txt", "w", encoding="utf-8")

# f.write("안녕하세요")
# f.close()

# text = input("아무거나 입력 : ")

# with open("file/test1.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# 점심 = ["돈가스", "짜장면", "탕수육", "떡볶이", "감자탕"]

# with open("file/test2.txt", "w", encoding="utf-8") as f:
#     for 밥 in 점심:
#         f.write(밥+"\n")


# 점심 = []

# with open("file/test2.txt", "r", encoding="utf=8") as f:
#     for line in f:
#         점심.append(line.replace("\n",""))

# print(점심)

# with open("file/test2.txt", "a", encoding="utf-8") as f:
#     f.write("라면")


# with open("file/image.jpg", "rb") as f:         
#     img = f.read()

# print(img)

# 문제1. input 함수로 입력받은 값을 note.txt에 저장하시오

# text = input("입력 : ")

# with open("file/note.txt", "w", encoding="utf-8") as f:
#     f.write(text)


# 문제2. 회원가입을 받아서 파일로 저장하세요
# 회원 정보는 이름, 이메일, 비밀번호, 나이
# 파일 이름은 회원의 이메일 @ 앞부분이 파일 이름입니다.
# 파일 형식은 txt 입니다.

# email = input("이메일: ").strip()
# file_name = email[:email.index("@")]

# account = []

# with open("file/"+ file_name, "w", encoding="utf-8") as f:
#     f.write(input("아이디: ").strip())
#     f.write(input("비번: ").strip())
#     (f.write(email)

name = input("이름 : ")
email = input("이메일 : ")
password = input("비밀번호 : ")
age = input("나이 : ")

user = [name, email, password, age]
file_name = "file/"+email[:email.index("@")]+".txt"

with open(file_name, "w", encoding="utf-8") as f:

    print(name,file=f)
    print(email,file=f)
    print(password,file=f)
    print(age,file=f)
 