import cv2
import numpy as np

img = cv2.imread("blobs.jpg")

if img is None:
    print("Image Not Loaded")
    exit()

grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(grey,190,255,cv2.THRESH_BINARY_INV)

params=cv2.SimpleBlobDetector_Params()

params.filterByColor = True
params.blobColor = 255
params.filterByArea = True
params.minArea = 2000
params.maxArea = 200000
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False

detector=cv2.SimpleBlobDetector_create(params)

keypoints=detector.detect(thresh)
print("Blobs Detected:", len(keypoints))
output=cv2.drawKeypoints(img,keypoints,None,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.namedWindow("Blob Detection",cv2.WINDOW_NORMAL)
cv2.imshow("BLOB DETECTION",output)
cv2.waitKey(0)
cv2.destroyAllWindows()
