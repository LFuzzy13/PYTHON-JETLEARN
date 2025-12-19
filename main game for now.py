#very important stuff
import pygame
from pygame.locals import *
from time import *
#other important stuff
pygame.init()

screen = pygame.display.set_mode((582,493))

pygame.display.set_caption(("MY NAME IS ISAAC NEWTONNNNNN"))

player_x = 150
player_y = 150

keys = [False,False,False,False]

player = pygame.image.load("player.png")
background = pygame.image.load("bg.png")

pygame.display.update()

#main stuff

while player_y < 800:
    screen.blit(background,(0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #if it quits le game
            pygame.quit()
            exit(0)

#keyssssss
        if event.type == pygame.KEYDOWN:
            #check where ye gannin
            if event.key == K_UP:
                keys[0]=True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            #check where ye gannin 2
            if event.key == K_UP:
                keys[0]=False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] = False

    if keys [0]:
           if player_y>0:
              player_y -= 7
    elif keys [2]:
            if player_y < 536:
               player_y += 7

    if keys [1]:
            if player_x>0:
                player_x -=2

    elif keys [3]:
            if player_x <536:
                player_x += 2
#updating gravity stuffffff
    player_y += 5
    sleep (0.05)

white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)
purpel = (128,0,128)
print ("game overrrr")
font = pygame.font.Font("Times New Roman", 32)
text = font.render('Game Over', True, purpel, white)
screen.blit(text,(250,300))
pygame.display.update()

        
                
                
            
            

    
            
