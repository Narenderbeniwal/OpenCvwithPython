from curses.ascii import FF

import cv2
print("Package imported")

#img = cv2.imread("img.jpeg")
#cv2.imshow("Output", img)
#cv2.waitKey(10000)


#cap = cv2.VideoCapture("/Users/ekcs011/Desktop/Tenet (2020) [720p] [BluRay] [YTS.MX]/Tenet.mp4")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0*FF == ord('q'):
        break
