import cv2
import numpy as np

img = cv2.imread("eyes2.png")

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey_blur = cv2.GaussianBlur(grey,(9,9),2)
detected_circles= cv2.HoughCircles(
    grey_blur,
    cv2.HOUGH_GRADIENT,
    dp=1.1,
    minDist=35,
    param1=50,
    param2=22,
    minRadius=12,
    maxRadius=35
)

if detected_circles is not None:
    detected_circles= np.uint16(np.around(detected_circles))
    for pt in detected_circles[0,:]:
        a,b,r = pt[0],pt[1],pt[2]
        cv2.circle(img,(a,b),r,(0,255,0),2)
        cv2.circle(img,(a,b),2,(0,0,255),3)

cv2.imshow("detected_circles",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
