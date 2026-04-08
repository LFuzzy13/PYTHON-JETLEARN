import cv2

image = cv2.imread("DETAIL2.png",1)

borderedimage=cv2.copyMakeBorder(image,5,5,5,5,cv2.BORDER_CONSTANT,value=(0,0,0))

cv2.imshow("bordered image",borderedimage)
cv2.waitKey(0)
cv2.destroyAllWindows()