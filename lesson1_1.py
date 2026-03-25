import cv2
import os

img=cv2.imread("pikaichu.png",1)
B,G,R=cv2.split(img)
cv2.imshow("original_image1",img)
cv2.waitKey(0)

cv2.imshow("bluesaturationimage",B)
cv2.imwrite("blue.png",B)
cv2.waitKey(0)


cv2.imshow("greensaturationimage",G)
cv2.imwrite("Green.png",G)
cv2.waitKey(0)

cv2.imshow("redsaturationimage",R)
cv2.imwrite("Red.png",R)
cv2.waitKey(0)
cv2.destroyAllWindows()
