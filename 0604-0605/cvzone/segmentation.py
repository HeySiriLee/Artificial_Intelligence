# p311_python:conda

import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(1)
segmentor = SelfiSegmentation(model=0)

while True:
    rectangel, frame = cap.read()

    imgOut = segmentor.removeBG(frame, imgBg=(255, 255, 255), cutThreshold = 0.1)
    imgStacked = cvzone.stackImages([frame, imgOut], cols=2, scale=1)

    # cv2.imshow("Segmentation", imgOut)
    cv2.imshow("Segmentation", imgStacked)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
