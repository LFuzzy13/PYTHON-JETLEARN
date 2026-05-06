import cv2
import numpy as np

img = np.full((500,500,3),(25,25,25),dtype="uint8")

#triangle
points=np.array([[250,100],[100,400],[400,400]])
points=points.reshape((-1,1,2))
cv2.fillPoly(img,[points],(45,45,45))
#pentagon
points=np.array([[250,80],[100,200],[150,400],[350,400],[400,200]])
cv2.fillPoly(img,[points],(25,25,25))
#circle
cv2.circle(img,(250,250),165,(35,25,35),-1)
#circle
cv2.circle(img,(250,250),150,(45,35,45),-1)
#diamond
points=np.array([[250,100],[100,250],[250,400],[400,250]])
cv2.fillPoly(img,[points],(200,50,200))
#circle
cv2.circle(img,(250,250),80,(250,100,250),-1)
#diamon2
points=np.array([[250,125],[172,250],[250,375],[325,250]])
cv2.fillPoly(img,[points],(255,155,255))
#circle
cv2.circle(img,(250,250),50,(255,175,255),-1)
#circle
cv2.circle(img,(250,250),25,(255,225,255),-1)
#circle
cv2.circle(img,(250,250),15,(255,255,255),-1)
#line
cv2.line(img,(110,400),(390,400),(45,45,45),12) 
#arrow
cv2.arrowedLine(img,(250,0),(250,115),(45,45,45),15)
#rectangle
cv2.rectangle(img,(100,400),(400,500),(45,45,45),-1)
#diamond
points=np.array([[100,400],[60,500],[400,400],[440,500]])
cv2.fillPoly(img,[points],(45,45,45))
cv2.imshow("the cube",img)
cv2.waitKey(0)
cv2.destroyAllWindows()