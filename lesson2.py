import cv2
import numpy as np

image = cv2.imread("STICK1.png")
image2=cv2.imread("STICK2.png")
image2=cv2.resize(image2,(image.shape[1],image.shape[0]))
weightedsum=cv2.addWeighted(image,0.5,image2,0.5,0)
cv2.imshow("weighted image",weightedsum)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("STICK1.png")
image2=cv2.imread("STICK2.png")
image2=cv2.resize(image2,(image.shape[1],image.shape[0]))
sub=cv2.subtract(image,image2)
cv2.imshow("subtracted image",sub)
cv2.waitKey(0)
cv2.destroyAllWindows()
