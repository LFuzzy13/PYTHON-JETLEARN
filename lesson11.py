#face detection, part 1

import cv2
import sys
import numpy
import os
import time

haar_file = "haarcascade_frontalface_default.xml"

datasets = "datasets"

sub_data = "JLM"

path = os.path.join (datasets,sub_data)

if not os.path.isdir(path):
    os.makedirs(path)

(width,height) = (180,120)
start_time = time.time()

face_cascade = cv2.CascadeClassifier(haar_file)
webcam=cv2.VideoCapture(0)
count = 1
while count < 40 and (time.time()-start_time)<60:
    (_,im) = webcam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y+h,x:x+w]
        face_resize = cv2.resize(face,(width,height))
        cv2.imwrite("%s/%s.png" % (path,count),face_resize)
        count +=1
    cv2.imshow("frecog",im)
    key = cv2.waitKey(10)
    if key == 27:
        break 
webcam.release()
cv2.destroyAllWindows()
    


