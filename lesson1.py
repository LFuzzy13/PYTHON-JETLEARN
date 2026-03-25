import cv2
import os

img = cv2.imread("pikaichu.png",cv2.IMREAD_COLOR)
cv2.imshow("original_image",img)

img2 = cv2.imread("pikaichu.png",0)
cv2.imshow("greyscale_image",img2)

savep_directory=r"C:\Users\Littl\OneDrive\Desktop\items\Jetlearn Code\OpenCV"
os.chdir(savep_directory)
cv2.imwrite("new_image_1.jpg",img2)
cv2.waitKey(5000)
cv2.destroyAllWindows()

