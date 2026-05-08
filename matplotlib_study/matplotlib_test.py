# matplotlib_test.py

'''

125번 png와 json파일을 사용하여 다음을 만들어 보세요

이미지 안에서 차량의 크기가 가장 큰 차와
크기가 세번째로 큰 차를 바운딩 박스로 표시해 주세요
가장 큰차의 바운딩 박스 테두리 색은 red
세번째로 큰차의 바운딩 박스 테두리색은 yellow


'''

'''
우선 png를 img로 가져와서 plt.imshow()/plt.show()
테두리 만들어주기. patches
테두리 박스의 좌표나 크기 값은 json 이용
json은 with 구문으로

색깔은?

'''

# 어떻게 가장 큰, 세 번째로 큰 객체를 뽑아낼 수 있을까나? list? dict? sorted? area? enumerate?

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json

# 이미지 파일 가져오기
img = plt.imread('18396708_frame_125.png')

# 제이슨 데이터 가져오기
with open("18396708_frame_125.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

plt.imshow(img)
ax = plt.gca()

max = 0
max2 = 0
max3 = 0
max_find = list()

for ann in data['frames']['annotations']:
    area = ann['label']['width'] * ann['label']['height']
    print(area)


for ann in data['frames']['annotations']:
    area = ann['label']['width'] * ann['label']['height']
    if area > max:
        max = area
    elif max > area > max2:
        max2 = area
    elif max2 > area > max3:
        max3 = area

# 조건문 순서 변경
for ann_ in data['frames']['annotations']:
    area_ = ann_['label']['width'] * ann_['label']['height']
    if area_ == max:
        max_find.append(ann_)
    elif area_ == max3:
        max_find.append(ann_)

print(max_find)

max_box = dict()
max_box['x'] = max_find[0]['label']['x']
max_box['y'] = max_find[0]['label']['y']
max_box['width'] = max_find[0]['label']['width']
max_box['height'] = max_find[0]['label']['height']

max3_box = dict()
max3_box['x'] = max_find[1]['label']['x']
max3_box['y'] = max_find[1]['label']['y']
max3_box['width'] = max_find[1]['label']['width']
max3_box['height'] = max_find[1]['label']['height']



box1 = patches.Rectangle((max_box['x'], max_box['y']),
                        max_box['width'], max_box['height'],
                        fill=False,
                        edgecolor='red',
                        linewidth=3)
box2 = patches.Rectangle((max3_box['x'], max3_box['y']),
                        max3_box['width'], max3_box['height'],
                        fill=False,
                        edgecolor='yellow',
                        linewidth=3)




ax.add_patch(box1)
ax.add_patch(box2)




plt.show()