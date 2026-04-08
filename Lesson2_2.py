import cv2
import numpy as np

image = cv2.imread("DETAIL2.png",0)



kernel=np.ones((5,5),np.uint8)
eroded_image = cv2.erode(image,kernel)
cv2.imshow("eroded image",eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()