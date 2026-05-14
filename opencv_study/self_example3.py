'''
문제 1 — putText 기초 ⭐
이미지 파일을 불러와서 아래 조건대로 텍스트를 출력하세요.

텍스트: "Hello OpenCV"
위치: 이미지 왼쪽 위 근처 (30, 60)
폰트: FONT_HERSHEY_SIMPLEX, 크기 1.5, 두께 2
색상: 초록색
결과 창을 띄우고 아무 키나 누르면 닫히게 하세요


'''
import cv2
import numpy as np

# img = cv2.imread("opencv_study/images/bird.png")

# copy_img = img.copy()

# cv2.putText(
#     copy_img,
#     "Hello openCV",
#     (30, 60),
#     cv2.FONT_HERSHEY_SIMPLEX,
#     1.5,
#     (0,255,0),
#     2
# )

# cv2.imshow("img",copy_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''
문제 2 — absdiff 이해 ⭐⭐
동영상에서 프레임을 연속으로 읽으면서 이전 프레임과 현재 프레임의 차이를 화면에 보여주세요.

조건:

두 프레임 모두 흑백으로 변환 후 비교
absdiff 결과를 "diff" 창으로 표시
ESC 키로 종료
힌트: pre_frame = None 패턴으로 시작하세요.

'''

# cap = cv2.VideoCapture("opencv_study/videos/bird.mp4")

# fps = cap.get(cv2.CAP_PROP_FPS)
# delay = int(1000/fps)

# pre_frame = None

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     cut = cv2.resize(frame, None, fx=0.5, fy=0.5 )

#     gray = cv2.cvtColor(cut, cv2.COLOR_BGR2GRAY)

#     if pre_frame is None:
#         pre_frame = gray
#         continue

#     diff = cv2.absdiff(pre_frame, gray)

#     pre_frame = gray    

#     cv2.imshow("video",diff)
#     if cv2.waitKey(delay) == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()




'''
문제 3 — 모폴로지 파이프라인 ⭐⭐
아래 순서대로 동영상 프레임을 처리하는 코드를 작성하세요.


흑백변환 → threshold(이진화) → MORPH_OPEN → MORPH_CLOSE → dilate
각 단계 결과를 별도 창(thresh, opened, linked, result)으로 보여주세요.

커널은 np.ones((5,5), np.uint8) 사용.

'''

# cap = cv2.VideoCapture("opencv_study/videos/bird.mp4")

# fps = cap.get(cv2.CAP_PROP_FPS)
# delay = int(1000/fps)

# pre_frame = None

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     cut = cv2.resize(frame, None, fx=0.5, fy=0.5 )

#     gray = cv2.cvtColor(cut, cv2.COLOR_BGR2GRAY)

#     _r, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

#     kernel = np.ones((5,5), np.uint8)

#     opend = cv2.morphologyEx(
#         thresh, cv2.MORPH_OPEN,
#         kernel, iterations=1
#     )

#     linked = cv2.morphologyEx(
#         opend, cv2.MORPH_CLOSE,
#         kernel, iterations=1
#     )

#     di = cv2.dilate(linked, None, iterations=1)

#     cv2.imshow("thresh",thresh)
#     cv2.imshow("opend",opend)
#     cv2.imshow("linked",linked)
#     cv2.imshow("result",di)
#     if cv2.waitKey(delay) == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

'''

문제 4 — 움직임 감지 + 바운딩박스 ⭐⭐⭐
동영상에서 움직이는 물체에 빨간 박스를 그리고 "motion" 텍스트를 표시하세요.

조건:

absdiff + threshold + dilate 파이프라인 사용
findContours로 윤곽선 추출
너무 작은 윤곽선(면적 400 미만)은 무시
boundingRect로 박스 위치 계산
rectangle + putText로 표시

'''


cap = cv2.VideoCapture("opencv_study/videos/bird.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)

# fps = cap.get(cv2.CAP_PROP_FPS)
# delay = int(1000/fps)


pre_frame = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cut = cv2.resize(frame, None, fx=0.5, fy=0.5)

    gray = cv2.cvtColor(cut, cv2.COLOR_BGR2GRAY)

    if pre_frame is None:
        pre_frame = gray
        continue

    diff = cv2.absdiff(pre_frame, gray)

    pre_frame = gray

    _, thresh = cv2.threshold(
        diff, 30, 255, cv2.THRESH_BINARY
    )

    di = cv2.dilate(thresh, None, iterations=1)

    contours, hire = cv2.findContours(
        di,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = cut.copy()
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area <= 400:
            continue

        x,y,w,h = cv2.boundingRect(cnt)

        cv2.rectangle(
            result,
            (x,y),
            (x+w,y+h),
            (0,0,255),
            2
        )

        cv2.putText(
            result,
            "motion",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )
    cv2.imshow("result", result)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()


'''

문제 5 — MOG2 vs absdiff 비교 ⭐⭐⭐
같은 동영상에 두 방법을 동시에 적용하고 결과를 나란히 띄우세요.

창 이름	방법
"absdiff"	absdiff + threshold
"mog2"	createBackgroundSubtractorMOG2 + apply
둘의 차이를 눈으로 비교해보세요.


'''

'''

문제 6 (도전) — 사람만 잡기 ⭐⭐⭐⭐
walk.mp4 영상에서 사람에만 박스를 치세요.

조건:

MOG2 배경 제거기 사용
면적 필터: 500 < area < 2000만 통과
세로가 가로보다 길어야 통과 (h > w)
통과한 것에만 rectangle + putText
이 조건들이 왜 필요한지 생각해보세요.

'''
