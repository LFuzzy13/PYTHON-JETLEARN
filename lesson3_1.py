import cv2

img = cv2.imread("DETAIL IMAGE 1.png",1)
(width,height)=img.shape[:2]
#pad=max(width,height)
#padded=cv2.copyMakeBorder(img,pad,pad,pad,pad,cv2.BORDER_CONSTANT,value=(0,0,0))
#(new_W,new_H)=padded.shape[:2]

matrix=cv2.getRotationMatrix2D((width/2,height/2),45,1)

res=cv2.warpAffine(img,matrix,(width,height))

cv2.imwrite("rotated_image.png",res)

cv2.imshow("original image",img)
cv2.waitKey(0)

cv2.imshow("rotated image",res)
cv2.waitKey(0)

cv2.destroyAllWindows()