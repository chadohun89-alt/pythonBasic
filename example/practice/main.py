'''
1번 문제 (FastAPI 기초)
새 파일 main.py를 만들어서 아래 조건을 만족하는 FastAPI 서버를 작성해보세요.


GET /hello
→ {"message": "안녕하세요"}

GET /hello/{name}
→ {"message": "안녕하세요, 홍길동님"}  (name에 넣은 값으로)
uvicorn main:app --reload로 실행
브라우저에서 http://localhost:8000/hello 확인
http://localhost:8000/docs 에서 Swagger 문서도 확인

'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def get_hello():
    message = {"message":"안녕하세요"}
    return message

@app.get("/hello/{name}")
def get_hello_name(name:str):
    message = {"message":f"안녕하세요,{name}님"}
    return message


'''
2번 문제 (FastAPI — 쿼리 파라미터)
main.py에 아래 엔드포인트를 추가해보세요.


GET /introduce
→ {"message": "저는 이름이고, 나이살입니다."}
조건:

URL로 name과 age를 받아서 메시지에 넣기
예) http://localhost:8000/introduce?name=홍길동&age=20
→ {"message": "저는 홍길동이고, 20살입니다."}
힌트 — 쿼리 파라미터는 경로에 {} 없이 함수 파라미터로만 선언하면 됩니다.

'''

@app.get("/introduce")
def get_introduce(name:str,age:int):
    message = {"message":f"저는 {name}이고, 나이는 {age}살입니다."}
    return message


'''
3번 문제 (FastAPI — POST + Pydantic)
main.py에 아래 엔드포인트를 추가해보세요.


POST /join
→ {"message": "홍길동님 가입을 환영합니다. 나이는 20살이시군요!"}
조건:

name(str)과 age(int)를 **요청 body(JSON)**로 받기
Pydantic 모델 JoinRequest 만들어서 사용하기
브라우저 대신 http://localhost:8000/docs 에서 테스트
힌트


from pydantic import BaseModel

class JoinRequest(BaseModel):
    name: str
    age: int

@app.post("/join")
def join(data: JoinRequest):
    # data.name, data.age 로 접근
    ...

'''



class JoinRequest(BaseModel):
    name:str
    age:int

@app.post("/join")
def add_join(data:JoinRequest):
    message = {"message": f"{data.name}님 가입을 환영합니다. 나이는 {data.age}살이시군요!"}
    return message


'''
4번 문제 (FastAPI — StreamingResponse로 이미지 반환)

GET /image
→ 이미지 파일을 HTTP 응답으로 반환
조건:

아무 이미지 파일 하나(test.png 등)를 practice 폴더에 넣기
FileResponse로 그 이미지를 반환하기
브라우저에서 http://localhost:8000/image 접속하면 이미지가 보여야 함
힌트


from fastapi.responses import FileResponse

@app.get("/image")
def get_image():
    return FileResponse("파일명.png", media_type="image/png")

'''

