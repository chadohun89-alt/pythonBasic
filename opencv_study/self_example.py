'''
문제 1.
surfer.png 를 읽어서 좌우 반전시킨 뒤 화면에 출력하세!
'''

import cv2

# img = cv2.imread("opencv_study/images/surfer.png")

# copy_img = img.copy()

# flip = cv2.flip(copy_img, 1)

# cv2.imshow("flip", flip)
# cv2.waitKey(0)

'''
문제 2.
dog.png 를 읽어서 세로 길이를 200px 기준으로 비율을 유지하며 리사이즈한 뒤 저장하세요.
(힌트: 오늘 실습에서는 가로 기준이었는데, 이번엔 세로 기준입니다)

'''
# 읽기
# 리사이즈
# 저장
# 보여주기

# 읽기, 복사
# img = cv2.imread("opencv_study/images/dog.png")
# copy_img = img.copy()

# 리사이즈 / resize(파일, (가로,세로))

# print(copy_img.shape)

# y, x, channel = copy_img.shape
# ratio = 200/y

# size = (int(y*ratio), int(x*ratio))

# resize = cv2.resize(copy_img, (size[1],size[0]))

# cv2.imwrite("opencv_study/images/resize_dog.png", resize)


'''
문제 3.
cat.png 를 읽어서 아래 순서대로 처리한 뒤 result_cat.png 로 저장하세요.

가로 150px 비율 유지 리사이즈
흑백 변환
GaussianBlur 적용 (7, 7)
threshold 적용 (기준값 100, THRESH_BINARY)


'''
# 읽기 imread
# 리사이즈 resize
# 흑백변환 cvtColor
# 블러처리 GaussianBlur
# 경계설정 threshold
# 저장 imwrite

# 읽기
img = cv2.imread("opencv_study/images/cat.png")
copy_img = img.copy()
print(copy_img.shape)

# 리사이즈
y, x, channel = copy_img.shape
ratio = 150/x
size = ( int(ratio*x), int(ratio*y))
print(size)
cut = cv2.resize(copy_img, size)


# 흑백변환
gray = cv2.cvtColor(cut, cv2.COLOR_BGR2GRAY)


# 블러처리
blur = cv2.GaussianBlur(gray, (7,7), 0)

# 경계설정
_r, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

# 저장
cv2.imwrite("opencv_study/images/q3.png",thresh)

#확인
confirm = cv2.imread("opencv_study/images/q3.png")
cv2.imshow("confrim", confirm)
cv2.waitKey(0)



'''
문제 4.
dog.png 를 읽어서 상하좌우 동시 반전 후 흑백 변환까지 한 뒤 화면에 출력하세요.

'''

'''
문제 5. (도전)
surfer.png 를 읽어서

가로를 320px로 비율 유지 리사이즈
GaussianBlur (5, 5) 로 노이즈 제거
threshold를 THRESH_BINARY_INV 로 적용 (기준값 150)
결과를 원본과 나란히 imshow 로 동시에 띄우기 (창 이름을 각각 "원본", "결과" 로 설정)

'''