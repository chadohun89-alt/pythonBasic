# json_test3.py

'''

18396595_frame_12.json 에서 사람을 찾고 사람의 좌표를 출력하세요.

'''

# 1. 파일 열기
# 2. 애노테이션들 반복문 돌리기
# 3. 카테고리 person인 경우 찾기
# 4. 좌표 담기.
# 5. 출력 하기.

import json

# with open("file/18396595_frame_12.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# anno = data["frames"]["annotations"]

# mans = list()

# for ann in anno:
#     if ann["category"]["code"] == "person":
#         mans.append(ann)

# for man in mans:
#     print(f"닝겐의 위치 (x좌표 : {man['label']['x']} / y좌표 : {man['label']['y']})")


with open("file/18396595_frame_12.json", "r", encoding="utf-8") as f:
    data = json.load(f)

annotations = data["frames"]["annotations"]

for ann in annotations:
    if ann["category"]["code"] == "person":
        x = ann["label"]["x"]
        y = ann["label"]["y"]

        print (f"사람 발견 했다!! x = {x}, y = {y}")
