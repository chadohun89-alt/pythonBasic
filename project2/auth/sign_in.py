# sign_in.py

import valid as _v
# from data import db as _db
from member_service import login

def signIn(id,pw):
    if not _v.id_len_check(id):
        print("아이디는 4 ~ 12자 입니다.")
    elif not _v.pw_len_check(pw):
        print("비밀번호는 6자 이상입니다.")
    else:
        return login.login_process(id,pw)


    # else:
    #     uid, upw - _db.find_by_id(id)
    #     if uid == id and upw == pw:
    #         print("로그인 성공")
    #     else:
    #         print("아이디 또는 비밀번호가 잘못되었습니다.")


# def sign(id):
#     uid, upw = db.find_by_id(id)
#     print(valid.id_len(uid))
#     print(valid.pw_lne(upw))