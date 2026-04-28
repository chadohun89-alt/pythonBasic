# main.py

from member_service import login
from auth import sign_in

print(login.login_process("gold", "123456"))


# '''

# auth 폴더 생성
#     - valid.py
#     - sign_in.py

#     valid.py - 아이디 길이 체크, 비밀번호 최소 길이 체크 하는 함수
#     sign_in.py - valid.py 사용, db.py 사용, 로그인처리

#     아이디 길이는 4 ~ 12자, 비밀번호는 최소 6자

# '''

sign_in.sign("gold")