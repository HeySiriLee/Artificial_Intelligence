# p311_python:conda

import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(1)

detector = PoseDetector(
    staticMode = False,
    modelComplexity = 1,
    smoothLandmarks = True,
    enableSegmentation = False,
    smoothSegmentation = True,
    detectionCon = 0.5,
    trackCon = 0.5
)

while True:
    rectangle, frame = cap.read()

    image = detector.findPose(frame)
    lmList, bboxInfo = detector.findPosition(
        image, draw=True,bboxWithHands=False
    )

    cv2.imshow("Pose", image)