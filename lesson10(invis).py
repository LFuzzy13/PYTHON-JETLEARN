import cv2
import numpy as np
import time 

print("opencv version :", cv2.__version__)

capture_video = cv2.VideoCapture("INVISIVID3.mp4")

time.sleep(0.03)

WIDTH = int(capture_video.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(capture_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = capture_video.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 60

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    "invisibleoutput.mp4",
    fourcc,
    fps,
    (WIDTH,HEIGHT)

)

background = None
for i in range(60):
    ret,background = capture_video.read()
    if not ret:
        continue

background = np.flip(background,axis=1)
delay = 1
frame_count = 0
while capture_video.isOpened():
    ret,img = capture_video.read()
    if not ret:
        break
    frame_count +=1
    img = np.flip(img,axis=1)
    HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red_one = np.array([20, 40, 60])
    upper_red_one = np.array([40, 255, 255])
    lower_red_two = np.array([40, 40, 60]) 
    upper_red_two = np.array([80, 255, 255])
    mask1 = cv2.inRange(HSV,lower_red_one,upper_red_one)
    mask2 = cv2.inRange(HSV,lower_red_two,upper_red_two)
    mask = mask1+mask2

    kernel = np.ones((3,3),np.uint8)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask = cv2.dilate(mask,kernel)
    mask_inv = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(background,background,mask=mask)
    res2 = cv2.bitwise_and(img,img,mask=mask_inv)
    finaloutput = cv2.add(res1,res2)
    cv2.imshow("invisivid",finaloutput)
    out.write(finaloutput)
    key = cv2.waitKey(delay)& 0xFF
    if key == 27:
        break
    if cv2.getWindowProperty("invisivid",cv2.WND_PROP_VISIBLE)<1:
        break

capture_video.release()
out.release()
cv2.destroyAllWindows()
print("video file saved sucessfully")


