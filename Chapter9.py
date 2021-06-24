import cv2

faceCascade = cv2.CascadeClassifier("/Users/ekcs011/Downloads/Face Detect/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("face.jpeg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.waitKey(0)