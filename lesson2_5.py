import cv2
import numpy as np

image = cv2.imread("DETAIL2.png",1)

borderedimage=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_REFLECT,value=(0,0,0))


gaussian=cv2.GaussianBlur(borderedimage,(5,5),0)
cv2.imshow("GAUSSIAN",gaussian)
cv2.waitKey(0)

median=cv2.medianBlur(image,7)
cv2.imshow("MEDIAN",median)
cv2.waitKey(0)

cv2.destroyAllWindows()

