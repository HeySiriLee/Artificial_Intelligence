import cv2
import dlib

cap = cv2.VideoCapture("./trained/lover.mp4")

if not cap.isOpened():
    print("Error opening video file")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("Fairy dining table - Seungwoo Cho", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Fairy dining table - Seungwoo Cho", 960, 540)

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("./trained/shape_predictor_5_face_landmarks.dat")

while True:
    ret, frame = cap.read()

    if not ret:
        print("No more frames in the video")
        break

    resized_frame = cv2.resize(frame, (960, 540), interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    dets = detector(gray, 1)

    for det in dets:
        x, y, w, h = det.left(), det.top(), det.width(), det.height()

        cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Fairy dining table - Seungwoo Cho", resized_frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
