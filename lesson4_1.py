import cv2
import numpy as np

img = np.ones((500,500,3),dtype="uint8")
cv2.rectangle(img,(1,1),(500,500),(255,200,130),-1)
cv2.line(img,(250,250),(250,499),(33,33,33),12)
cv2.rectangle(img,(325,360),(180,150),(30,30,30),-1)
cv2.circle(img,(250,190),30,(1,1,250),-1)
cv2.circle(img,(250,250),30,(1,200,250),-1)
cv2.circle(img,(250,310),30,(1,250,1),-1)
cv2.imshow("drawing demo :)",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
