import cv2
import time

# 어디에서 가져올 것인가 (Source)
# Load a video
cap = cv2.VideoCapture("lover.mp4")

# 실시간으로 계속 영상 받기
while True:
    _, frame = cap.read()

    # Information frame
    print("현재 진행 프레임: ", cap.get(cv2.CAP_PROP_POS_FRAMES))
    print("현재 전체 프레임: ", cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Color video → B&W video
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Lover color video", frame)
    cv2.imshow("Lover grayFrame video", gray_frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()