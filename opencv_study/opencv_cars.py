# 차량이 몇대인지 구하시오
# 1. 읽기
# 2. 복사
# 3. 흑백전환
# 4. 경계설정
# 5. 외곽선

import cv2

# img = cv2.imread("opencv_study/images/car2.png")

# copy_img = img.copy()

# gray = cv2.cvtColor(copy_img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (19, 19), 0)
# _,thresh = cv2.threshold(blur, 135, 255, cv2.THRESH_BINARY_INV)

# contours, hire = cv2.findContours(
#     thresh,
#     cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_SIMPLE
# )

# result = img.copy()

# cv2.drawContours(result, contours, -1, (0,0,255), 2)

# print(f"차량 개수 : {len(contours)}")

# cv2.imshow("a",result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.imread("opencv_study/images/car2.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur( gray, (5,5), 0)

_,thresh = cv2.threshold(
    blur, 120, 255, cv2.THRESH_BINARY_INV
    )

contours, hire = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()
count = 0

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 200:
        count += 1

print("차량 수 : ", count)

cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()