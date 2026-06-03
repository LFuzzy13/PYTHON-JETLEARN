import os
import cv2
from PIL import Image

path = r"C:\Users\Littl\OneDrive\Desktop\OpenCV\images(PILLOW)"
os.chdir(path)

mean_height = 0
mean_width = 0

image_files = []

for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        image_files.append(file)

num_of_img = len(image_files)

for file in image_files:
    img = Image.open(os.path.join(path, file))
    width,height = img.size
    mean_width +=width
    mean_height += height

mean_width = mean_width // num_of_img
mean_height = mean_height // num_of_img

print("average width", mean_width)
print("average height", mean_height)

for file in image_files:
    img = Image.open(os.path.join(path,file))
    width,height = img.size
    print(width,height)
    imgResized = img.resize((mean_width,mean_height),Image.LANCZOS)
    imgResized.save(file,"JPEG",quality=95)
    print(file, "is resized.")

video_name = "VIDEOTEST1.avi"
frame = cv2.imread(image_files[0])
height,width,layers=frame.shape
fourcc = cv2.VideoWriter_fourcc(*"XVID")
video=cv2.VideoWriter(video_name,fourcc,1,(width,height))

for image in image_files:
    frame = cv2.imread(image)
    video.write(frame)

video.release()
cv2.destroyAllWindows()
print("video created sucessfully")

cap = cv2.VideoCapture(video_name)
while True:
    ret,frame=cap.read()
    if not ret:
        break

    cv2.imshow("Video Slideshow 1", frame)
    if cv2.waitKey(1000) & 0xff ==ord("q"):
        break

cap.release()
cv2.destroyAllWindows