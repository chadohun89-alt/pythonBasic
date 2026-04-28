# valid.py

#아이디 길이 체크 함수

def pw_len_check(pw):
    return len(pw >= 6)

def id_len_check(id):
    return len(id) >= 4 and len(id) <=12
    # if len(id) >= 4 and len(id)<=12:
    #   return True
    # else:
    #     return False  


# def id_len(id):
#     if len(id) >= 4 and len(id) <= 12:
#         return "아이디 길이 적절"
#     else:
#         return "아이디 길이 부적절"

# def pw_lne(pw):
#     if len(pw) <= 6:
#         return "비번 길이 적절"
#     else:
#         return "비번 길이 부적절"