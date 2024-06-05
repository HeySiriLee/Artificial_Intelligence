import easyocr
import cv2
import numpy as np

# Global variable
pointList = []
global_carnum = ''

# Import and pre-process images
imgFile = "./test_data/car03.jpg"

color_image = cv2.imread(imgFile, cv2.IMREAD_COLOR)
gray_image = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

def onChange(pos):
    pass

# A function to crop a selected box area 
# and transform it into a horizontally aligned rectangle
def selectBoxCut():
    global global_carnum

    # Extract the block
    src = np.float32(pointList)

    # Transform the image size
    width, height = 300, 80

    # Four points (clockwise)
    dst = np.array([
        [0, 0],
        [width, 0],
        [width, height],
        [0, height]
    ], dtype=np.float32)

    # Matrix transformation
    matrix = cv2.getPerspectiveTransform(src, dst)
    result1 = cv2.warpPerspective(color_image, matrix, (width, height))
    result2 = cv2.warpPerspective(binary, matrix, (width, height))

    cv2.imshow('Car number_Color', result1)
    cv2.imshow('Car number_Binary', result2)

    # Save the file
    cv2.imwrite('./result_data/car03_num.jpg', result2)

    # License plate recognition
    reader = easyocr.Reader(['en', 'ko'])

    result = reader.readtext('./result_data/car03_num.jpg')

    for message in result:
        print(message[1])
        global_carnum = message[1]
        break

# Function to draw coordinates
def pointDraw():
    tmpImg = color_image.copy()

    i = 0
    for data in pointList:
        cv2.circle(tmpImg, tuple(data), 10, (0, 255, 255), cv2.FILLED)
        
        # Draw a line
        if i >= 0:
            cv2.line(tmpImg, tuple(pointList[i-1]), tuple(pointList[i]), (0, 255, 0), 2, cv2.LINE_AA) 

        # Extract the bounding box 
        if i == 3:
            selectBoxCut()

        i += 1

    return tmpImg

# Functions that control the mouse
def mouse_handler(event, x, y, flags, param):
    global color_image, pointList

    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Click')
        pointList.append([x,y])
        print(pointList)

    if event == cv2.EVENT_RBUTTONUP:
        print('Write Click')
        if len(pointList) >= 2:
            cv2.rectangle(color_image, tuple(pointList[0]), (x, y), (0, 255, 0), 2)
            cv2.imshow("color_image", color_image)
        else:
            print("Select at least 2 points to draw rectangle")

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('Double Click')
        pointList = []

    # Drawing with Draw
    cv2.imshow("color_image", pointDraw())

# Make a track bar
winnames = 'TrackBar'
cv2.namedWindow(winnames)
cv2.imshow("color_image", color_image)
cv2.createTrackbar('threshold', winnames, 127, 255, onChange) 

# Control a mouse
# cv2.imshow("color_image", color_image)
cv2.setMouseCallback("color_image", mouse_handler)

# Control a track bar
while cv2.waitKey(1) != ord('q'):
    
    pos = cv2.getTrackbarPos('threshold', winnames)
    ret, binary = cv2.threshold(gray_image, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow(winnames, binary)

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('./test_data/car03_01.jpg', binary)

cv2.destroyAllWindows()