# -*- coding:utf-8 -*-

import pygame, sys,os
from pygame.locals import * 
import app


def main():
    # Start up pygame/make screen
    pygame.init() 
    window = pygame.display.set_mode((460, 320)) 
    screen = pygame.display.get_surface() 
    pygame.display.set_caption('Rabit Hazard') 
    # make background
    background = app.load_image("player.bmp", -1)
    # blit background on to the screen
    screen.blit(background, (0,0))
    pygame.display.flip()

    # load fonts
    
    # make the text needed



if __name__ == '__main__':
    main()
 
while True: 
   app.input(pygame.event.get()) 

