import pygame
from pygame.locals import *
import time

pygame.init()

screen = pygame.display.set_mode((600,600))
playerx = 200
playery = 200
keys = [False, False, False, False]

background = pygame.image.load("Rocket in space2/background.png")
player = pygame.image.load("Rocket in space2/rocket.png")

while playery < 600:
    screen.blit(background, (0,0))
    screen.blit(player, (playerx, playery))
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys[0] = True
            elif i.key == K_DOWN:
                keys[1] = True
            elif i.key == K_LEFT:
                keys[2] = True
            elif i.key == K_RIGHT:
                keys[3] = True

        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys[0] = False
            elif i.key == K_DOWN:
                keys[1] = False
            elif i.key == K_LEFT:
                keys[2] = False
            elif i.key == K_RIGHT:
                keys[3] = False

    if keys[0] == True:
        playery = playery - 2.5
    if keys[1] == True:
        playery = playery + 1.5
    if keys[2] == True:
        playerx = playerx - 2
    if keys[3] == True:
        playerx = playerx + 2

    playery = playery + 0.5
    

