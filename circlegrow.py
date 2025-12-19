#importing and initialising
import pygame
pygame.init()


#global variables
screen = pygame.display.set_mode([500,500])
red = (233,0,0)
green = (0,248,0)
blue = (0,0,139)
white = (233,233,233)
black = (6,7,6)
yellow = (234,134,0)

class Circle():
    def __init__(self, color, wid, rad, pos):
        self.scrn = screen
        self.color = color
        self.wid = wid
        self.pos = pos
        self.rad = rad 

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.wid, self.rad, self.pos)

    def grow(self,x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.wid, self.rad, self.pos)
 
#objectssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
position = (250,250)
redcircle = Circle(screen, red, 1, 30, position)
bluecircle=Circle(screen, blue, 2, 23, position)
greencircle=Circle(screen, green,5,58, position)
yellowcircle=Circle(screen, yellow, 7, 71, position)
pygame.display.update()


while(1):
    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            bluecircle.draw()
            redcircle.draw()
            yellowcircle.draw()
            greencircle.draw()
        elif(event.type == pygame.MOUSEBUTTONUP):
            bluecircle.grow(2)
            redcircle.grow(2)
            yellowcircle.grow(4)
            greencircle.grow(1)
            pygame.display.update()
        elif(event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackcircle = Circle(black, 5, 1, pos)
            blackcircle.draw()
            pygame.display.update()
            
        
        
        
