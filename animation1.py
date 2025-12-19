import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

s = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("animation V1.0")
img = pygame.image.load("backgroundoneimg.jpg")
image = pygame.transform.scale(img,(WIDHT,HEIGHT))

while (True):
    font=pygame.font.SysFont("Times New Roman",10)
    text=font.render("hello",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    siplay_surface.blit(text,(210,180))
    pygame.display.update()
    time.sleep(2)
