# -*- coding:utf-8 -*-

import pygame, sys,os
from pygame.locals import * 
import app

pygame.init() 
inputimg = app.load_image("player.bmp", -1)
window = pygame.display.set_mode((460, 320)) 
pygame.display.set_caption('Rabit Hazard') 
screen = pygame.display.get_surface() 
screen.blit(inputimg, (0,0))
pygame.display.flip()


while True: 
   app.input(pygame.event.get()) 
 
