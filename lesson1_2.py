import cv2 

image = cv2.imread("pikaichu.png",cv2.IMREAD_COLOR)
if image is None:
    print("image not found")
else:
    hsv_img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    cv2.imshow("original pika image",image)
    cv2.waitKey(0)
    cv2.imshow("pikaichu HSV",hsv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()