import cv2
import numpy as np

img = np.zeros((500,500,3),dtype="uint8")
cv2.line(img,(1,1),(499,499),(63,220,130),12)
cv2.rectangle(img,(310,310),(110,110),(100,230,250),-1)
cv2.circle(img,(100,100),23,(150,73,109),15)
cv2.circle(img,(320,320),23,(150,73,109),15)
cv2.putText(img,"Hello",(124,240),cv2.FONT_HERSHEY_TRIPLEX,2,(20,50,75))
cv2.imshow("drawing demo :)",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


