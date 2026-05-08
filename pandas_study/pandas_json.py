# pandas_json.py

import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['font.family'] = 'Malgun Gothic' #Malgun Gothic
plt.rcParams['axes.unicode_minus'] = False

with open('012_000000.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

annotations = [
    a for a in data["annotations"]
    if "category_name" in a
]

# 데이터 프레임으로 저장하기
df = pd.DataFrame(annotations)
counts = df['category_name'].value_counts()
print("트럭 : ", counts['truck'])

# 차량들의 너비 값 출력
car_width = df["bbox"].apply(lambda x:x[1][0])
print(car_width)


# 문제 너비가 가장 큰 차량을 찾으시오, 이미지에 바운딩박스 표시하기

# 차량을 찾는 방법은?
# 너비? max로 찾으면 되지 않나?

best_car_width = max(car_width)
print(best_car_width)

best_car = df[df["bbox"].apply(lambda x:x[1][0])==best_car_width]
print(best_car)

img = plt.imread('012_000000.jpg')
plt.imshow(img)

ax = plt.gca()

# best_car_x = best_car["bbox"].apply(lambda x:x[0][0])
best_car_x = best_car.iloc[0]["bbox"][0][0]
best_car_y = best_car.iloc[0]["bbox"][0][1]

best_car_box_width = best_car.iloc[0]["bbox"][1][0]
best_car_box_height = best_car.iloc[0]["bbox"][1][1]
print(best_car_x, best_car_y)

box = patches.Rectangle(
    (best_car_x, best_car_y),
    best_car_box_width,
    best_car_box_height,
    fill=False,
    edgecolor="red",
    linewidth=2
)

ax.add_patch(box)

plt.show()


# 이미지에 바운딩 박스 표시하는 방법은?
# (1. img 만들기 / 2. img 그리기 / 3. 객체 생성 / 4. 박스생성 / 5. 이미지에 박스 붙여넣기





# 문제 각 차량별 너비를 구하여 그래프로 출력해보세요
# 너비를 그래프로 출력? 그래프? 차량을 x축으로 너비를 y축으로

result = car_width
result.plot(kind='bar')

plt.title("차량 너비 그래프")
plt.ylabel("너비")
plt.xlabel("차번호")
plt.xticks(rotation=45)

plt.show()



