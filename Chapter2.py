import cv2
import numpy as np

img = cv2.imread("img.jpeg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations= 1)

cv2.imshow("Gray Image", imgGray)

cv2.imshow("Blur Image", imgBlur)

cv2.imshow("CannyImage", imgCanny)
cv2.imshow("DialationImage", imgDialation)
cv2.imshow("ErodedImage", imgEroded)
cv2.waitKey(0)