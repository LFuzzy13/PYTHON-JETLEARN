#face detection, part 1

import cv2
import sys
import numpy
import os

haar_file = "haarcascade_frontalface_default.xml"

datasets = "datasets"

sub_data = "JLM"

path = os.path.join (datasets,sub_data)

if not os.path.isdir(path):
    os.makedirs(path)

(width,height) = (180,120)
face_cascade = cv2.CascadeClassifier(haar_file)
webcam=cv2.VideoCapture(0)
count = 1
while count < 30:
    (_,im) = webcam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)
    