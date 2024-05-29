import cv2

# 어디에서 가져올 것인가 (Source)
# Control a! camera
cap = cv2.VideoCapture(0)

# Control a camera size
# width = 3, height = 4
cap.set(3, 1280)
cap.set(4, 720)

# 실시간으로 계속 영상 받기
while True:
    _, frame = cap.read()

    # Change right & left
    frame = cv2.flip(frame, 1)

    # Color video → B&W video
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Color video", frame)
    cv2.imshow("GrayFrame video", gray_frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()