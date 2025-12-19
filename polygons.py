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
class Polygon():
    def __init__(self,color,points,width):
        self.polygon_color = color
        self.polygon_surf = screen
        self.polygon_points = points
        self.polygon_width = width

    def draw(self):
        self.Draw_Polygon = pygame.draw.polygon(self.polygon_surf, self.polygon_color, self.polygon_points,self.polygon_width)

#making objects/instances of a class
GreenRect=Polygon(green,((50,20),(70,30)),20)
RedRect=Polygon(red,((150,200),(100,49)),58)
BlueRect=Polygon(blue,((250,300),(200,91)),97)

#accessing function "draw"
GreenRect.draw()
RedRect.draw()
BlueRect.draw()

#making it visible
pygame.display.update()



