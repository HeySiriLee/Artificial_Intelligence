# -*- coding: utf-8 -*-
# Check the opencv version
import cv2

print(cv2.__version__)

# Load image
# ver. Color
imageCol = cv2.imread("lover.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Lover version color", imageCol)

# ver. B & W
imageBandW = cv2.imread("lover.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Lover version black & white", imageBandW)

cv2.waitKey()
cv2.destroyAllWindows()