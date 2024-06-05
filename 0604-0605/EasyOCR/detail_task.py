import easyocr
import cv2
import numpy as np

# Global variable
pointList = []
global_areaCut = False

# Import and pre-process images
imgFile = "./test_data/car02_02.jpg"

color_image = cv2.imread(imgFile, cv2.IMREAD_COLOR)
gray_image = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

def onChange(pos):
    pass

# Function to draw coordinates
def pointDraw():
    global global_areaCut

    tmpImg = color_image.copy()

    i = 0
    for data in pointList:
        cv2.circle(tmpImg, tuple(data), 10, (0, 0, 255), cv2.FILLED)
    
    return tmpImg

# Functions that control the mouse
def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print('Click a Right Button')
        pointList.append([x,y])
        print(pointList)
    if event == cv2.EVENT_LBUTTONUP:
        print('Click a Left Button')
        pointList.pop()
        print(pointList)

    # Drawing with Draw
    cv2.imshow("color_image", pointDraw())

# make a track bar
winnames = 'TrackBar'
cv2.namedWindow(winnames)
cv2.imshow('color_img', color_image)
cv2.createTrackbar('threshold', winnames, 127, 255, onChange) 

# Control a mouse
cv2.setMouseCallback("color_image", mouse_handler)

# Control a track bar
while cv2.waitKey(1) != ord('q'):
    
    pos = cv2.getTrackbarPos('threshold', winnames)
    ret, binary = cv2.threshold(gray_image, pos, 255, cv2.THRESH_BINARY)
    
    cv2.imshow(winnames, binary)

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('./test_data/car02_05.jpg', binary)

cv2.destroyAllWindows()