import cv2
import numpy as np

cam = cv2.VideoCapture(0)

frameWidth = 500
frameHeight = 500

cam.set(3, frameWidth)
cam.set(4, frameHeight)

myColors = [[0,50,0,87,152,198]]

def findColor(image, colors):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow("Mask", mask)

def getContours(image1):
    contours, hierarchy = cv2.findContours(image1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cn in contours:
        area = cv2.contourArea(cn)
        if area>500:
            cv2.drawContours(imgResult, cn, -1, (255,0,0), 3)
            peri = cv2.arcLength(cn, True)
            approx = cv2.approxPolyDP(cn, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)

while True:
    success, img = cam.read()
    imgResult = img.copy()
    findColor(img, myColors)
    getContours(img)
    # Helps to convert color to gray scale live feed
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Result", imgResult)
    # cv2.imshow("Live feed", imgGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
