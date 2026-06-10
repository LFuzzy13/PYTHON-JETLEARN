from PIL import Image,ImageDraw
import cv2
import numpy as np
import math

WIDTH = 1000
HEIGHT = 800

FPS = 60
TOTAL_FRAMES = 1000

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter("Solar_system.mp4", fourcc, FPS, (WIDTH,HEIGHT))

planets = [("Mercury", 60, 5, (180,180,180), 0.08),
           ("Venus", 100, 8, (255,200,0), 0.06),
           ("Earth", 150, 9 ,(0,120,255), 0.05),
           ("Mars", 200,7,(255,80,80),0.04),
           ("Jupiter", 270,18,(210,180,140),0.03),
           ("Saturn",340,16,(240,220,120),0.025),
           ("Uranus", 410,12,(100,255,255), 0.02),
           ("Neptune",470,12,(50,50,255), 0.015)
           ]

stars = []

for i in range(400):
    x = np.random.randint(0,WIDTH)
    y = np.random.randint (0,HEIGHT)
    stars.append((x,y))

for frame in range(TOTAL_FRAMES):
    img = Image.new("RGB",(WIDTH,HEIGHT),(0,0,20))
    draw = ImageDraw.Draw(img)
    for x,y in stars:
     brightness = np.random.randint(150,256)

     draw.ellipse(
        (x -1, y - 1, x + 1, y + 1),
        fill = (brightness, brightness, brightness)
     )

    for planet in planets:
       orbit = planet[1]
       draw.ellipse(
          (CENTER_X - orbit, CENTER_Y - orbit, CENTER_X + orbit, CENTER_Y + orbit),
          outline = (50,50,50),
        )
    for glow in range(60,20, -5):
       draw.ellipse(
          (CENTER_X - glow, CENTER_Y - glow, CENTER_X + glow, CENTER_Y + glow),
          fill = (255,180,0)
        )
    draw.ellipse(
       (CENTER_X - 25, CENTER_Y - 25, CENTER_X + 25, CENTER_Y + 25),
       fill = (255,255,0)
     )

    earth_x = 0
    earth_y = 0

    for index,planet in enumerate(planets):
       name, orbit, size, color, speed = planet
       angle = frame * speed + index
       x  = CENTER_X + orbit * math.cos(angle)
       y = CENTER_Y + orbit * math.sin(angle)

       draw.ellipse(
          (x - size, y - size, x + size, y + size),
          fill = color
       )

       draw.text(
          (x + 12, y - 12),
          name,
          fill = "white"

       )

        
       if name == "Earth":
          earth_x = x
          earth_y = y

       if name == "Saturn":
          draw.ellipse((
             x - size - 10,
             y-size // 2,
             x + size + 10,
             y + size // 2),
             outline = (230,230,180),
             width = 2,
          ) 
    moon_angle = frame * 0.25
    moon_x = earth_x + 20 * math.cos(moon_angle)
    moon_y = earth_y + 20 * math.sin(moon_angle)

    draw.ellipse(
       (moon_x - 3, moon_y - 3, moon_x + 3, moon_y + 3),
       fill = (220,220,220)

    )
    np.array(img)

    frame_cv = cv2.cvtColor(
       np.array(img),
       cv2.COLOR_RGB2BGR

    )

    video.write(frame_cv)

    cv2.imshow(
       "solar system animation", frame_cv
    )

    if cv2.waitKey(1000 // FPS ) & 0xFF == ord("q"):
       break
video.release()
cv2.destroyAllWindows()
print ("animation saved succesfully")
print("file name : solar_system.mp4")

