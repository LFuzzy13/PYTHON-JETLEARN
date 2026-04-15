import cv2

img=cv2.imread("DETAIL IMAGE 1",1)
edges=cv2.Canny(img,100,200)
cv2.imshow("canny image innit",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()