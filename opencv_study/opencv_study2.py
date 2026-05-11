# opencv_study2.py

# AI가 영상분석을 하는데 먼저 전처리
# 전처리는 크기 변경, 흑백변환, 노이즈 제거, 강조 처리 등

import cv2
# img = cv2.imread("opencv_study/images/surfer.png")

# 변경 이후에 show
# 1. 흑백 변환 - cv2.COLOR_BGR2GRAY
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("surfer",gray)
# print(gray.shape)
# print(gray[100][100])
# cv2.waitKey(0)

# 2. 크기 변경 하기
# cv2.resize( 대상, (가로, 세로))

# small = cv2.resize(img, (152, 83))
# cv2.imshow("size",small)
# print(small.shape)
# cv2.waitKey(0)

# 3. 이미지 뒤집기(반전)
# flip = cv2.flip(img, 1)
# # 1 - 좌우 반전, 0 - 상하 반전, -1 - 상하좌우반전

# cv2.imshow("flip", flip)
# cv2.waitKey(0)

# 4. 블러 처리 - 이미지를 흐리게 만드는 것
# 노이즈 감소의 목적
# blur = cv2.GaussianBlur(img, (5,5), 0)
# #(5,5)의 값을 크게 주면 더더 흐려진다.

# cv2.imshow("blur",blur)
# cv2.waitKey(0)

# 5. 경계 - threshold
# gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
# _r, thresh =  cv2.threshold(
#     gray, 127, 255, cv2.THRESH_BINARY
# )

# _, thresh_rev = cv2.threshold(
#     gray, 127, 255, cv2.THRESH_BINARY_INV
# )

# print(_r)
# cv2.imshow("gray",gray)
# cv2.imshow("bin",thresh)
# cv2.imshow("inv",thresh_rev)
# cv2.waitKey(0)

# cv2.destroyAllWindows()

# 사진의 크기는 가로길이 320으로 비율 유지해서 변경하고
# 흑백 변환하고, 멍멍이가 잘 보일 수 있도록 경계설정하여
# dog_result.png 로 저장하기

# 1. 이미지 가져오기 imread
# 2. 크기 조절 resize
# 3. 흑백변환 cvtColor
# 4. 경계설정 threshold
# 5. 보기 imshow
# 6. 저장 imwrite(경로, 이미지?)

# 이미지 가져오기
img = cv2.imread("opencv_study/images/dog.png")
copy_img = img.copy()
print(copy_img.shape)

# 크기조절
ratio = 320/copy_img.shape[1]
size = [int(copy_img.shape[0]*ratio),int(copy_img.shape[1]*ratio)]
print(size)

cut = cv2.resize(copy_img, (size[1],size[0]))

# 흑백변환
gray = cv2.cvtColor(cut, cv2.COLOR_RGB2GRAY)

# 경계설정
_r, thres = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)


# 저장
cv2.imwrite("opencv_study/images/filter_dog.png", thres)
img2 = cv2.imread("opencv_study/images/filter_dog.png")

# 보기
cv2.imshow("filter",img2)
cv2.waitKey(0)

