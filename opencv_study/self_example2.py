# self_example2.py

'''
문제 1 — 동전 크기 구별

coin.png를 읽어서 동전마다 바운딩박스를 그리되,

면적이 가장 큰 동전 → 빨간색 박스
나머지 동전 → 초록색 박스
콘솔에는 "가장 큰 동전 면적: XXXX" 출력.

'''
# 파일 읽기
# 면적? 면적을 어떻게 가져오지? findContour
# 바운딩 박스 rectangle(이미지, 좌표, 좌표, 색, 선굵기)
# 콘솔출력 w * h



import cv2

img = cv2.imread("opencv_study/images/coin.png")

copy_img = img.copy()

gray = cv2.cvtColor(copy_img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9,9), 0)
_r, thresh = cv2.threshold(blur, 125, 255, cv2.THRESH_BINARY_INV)

contours, hire = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

max_cnt = ""
max_area = 0

for cnt in contours:
    area = cv2.contourArea(cnt)    
    if area > max_area:
        max_cnt = cnt

max_x, max_y, max_w, max_h = cv2.boundingRect(max_cnt)
cv2.rectangle(
    copy_img,
    (max_x, max_y),
    (max_x+max_w, max_y+max_h),
    (0,0,255),
    2
)

cv2.imshow("copy", copy_img)
cv2.imshow("a", thresh)
cv2.waitKey(0)



'''
문제 2 — 차량 번호 달기

car2.png에서 각 차량에 바운딩박스를 그리고,
박스 위쪽에 cv2.putText()로 차량 번호(1, 2, 3…)를 흰색 글자로 표시.

힌트: cv2.putText(img, "1", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

'''


'''
문제 3 — 영상 구간별 프레임 저장

bird.mp4에서 3초, 6초, 9초 지점의 프레임을 각각
frame_3s.png, frame_6s.png, frame_9s.png로 저장.

반복문으로 처리하되 cap.set() + cap.read() 조합 사용.

'''