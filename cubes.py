
#please read the notes at the bottom


#initiating and importing pygame library
import pygame
pygame.init()

#setting dimensions of the screeeeeeeen/making the screen be big :)
screen = pygame.display.set_mode((600,600))

#making the colourrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrs
red=(255,30,30)
green=(30,255,30)
blue=(30,30,255)
white=(253,253,253)
black=(2,2,2)
screen.fill(black)

#making that stuff visible
pygame.display.update()

#making the class
class Rect():
    def __init__(self,color,dimensions):
        self.rect_color = color
        self.rect_surf = screen
        self.rect_dimensions = dimensions
    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

#making objects/instances of a class
GreenRect=Rect(green,(50,20,100,100))
RedRect=Rect(red,(150,200,150,150))
BlueRect=Rect(blue,(250,300,250,250))

#accessing function "draw"
GreenRect.draw()
RedRect.draw()
BlueRect.draw()

#making it visible
pygame.display.update()

#please run this file in IDLE for best performance

