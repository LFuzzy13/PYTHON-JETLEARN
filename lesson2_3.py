import cv2
import numpy as np

image = cv2.imread("DETAIL2.png",1)
cv2.imshow("DETAIL2",image)
cv2.waitKey(0)
gaussian=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("GAUSSIAN",gaussian)
cv2.waitKey(0)
median=cv2.medianBlur(image,5)
cv2.imshow("MEDIAN",median)
cv2.waitKey(0)
bilateral=cv2.bilateralFilter(image,9,75,75)
cv2.imshow("BILATERAL",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()