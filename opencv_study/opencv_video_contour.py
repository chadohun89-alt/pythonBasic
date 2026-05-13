# opencv_video_contour.py

import cv2

cap = cv2.VideoCapture("opencv_study/videos/video2.mp4")

# 영상 fps
fps = cap.get(cv2.CAP_PROP_FPS)

delay = int( 1000/ fps ) # waitKey에 넣을 딜레이 계산
print(delay)

while True:
    ret, frame = cap.read()

    if not ret:
        print("영상 종료")
        break

    frame = cv2.resize( frame, (640, 480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _r, thresh = cv2.threshold(
        blur, 100, 255, cv2.THRESH_BINARY
        )
    

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # for cnt in contours:
    #     area = cv2.contourArea(cnt)
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     if area > 2000 :
    #         cv2.rectangle(
    #             frame,
    #             (x, y),
    #             (x+w, y+h),
    #             (0,0,255),
    #             2
    #         )
        


    print("객체 몇개:", len(contours))

    frame_copy = frame.copy() # 이미지값 변경 해야되니 복사본 만들기

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(
            frame_copy,
            (x,y),
            (x+w,y+h),
            (0,0,255),
            2
        )



    cv2.imshow("thresh", thresh)
    cv2.imshow("bounding", frame_copy)

    if cv2.waitKey(delay*2) == 27:
        print("종료")
        break

cap.release()
cv2.destroyAllWindows()

    
