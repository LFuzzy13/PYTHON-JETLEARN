import cv2
import numpy as np

img = cv2.imread("circles.jpg",cv2.IMREAD_GRAYSCALE)

if img is None:
    print ("Image Not Found, Please Try Again.")
    exit()

_,thresh = cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
thresh = cv2.GaussianBlur(thresh,(5,5),0)

params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 10
params.maxThreshold = 200

params.filterByColor = True
params.blobColor = 255
params.filterByArea = True
params.minArea = 1000
params.maxArea = 50000
params.filterByCircularity = True
params.minCircularity = 0.7
params.filterByConvexity = False
params.filterByInertia = False


detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(thresh)
output = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
output = cv2.drawKeypoints(output,keypoints,None,(10,10,250),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numberofblobs = len(keypoints)
print("Number Of Blobs Detectded:", numberofblobs)
cv2.putText(output,"Blobs Detected:"+str(numberofblobs),(20,40),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
display=cv2.resize(output,(900,600))
cv2.imshow("Blob Detection Image",display)
cv2.waitKey(0)
cv2.destroyAllWindows()
