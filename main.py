# -*- coding:utf-8 -*-

import pygame, sys,os
from pygame.locals import * 
import app, input
import stage1


#stage = ["title", "main", "stage1"]
stage = 3

def main():
    # Start up pygame/make screen
    pygame.init() 
    window = pygame.display.set_mode((460, 320)) 
    screen = pygame.display.get_surface() 
    pygame.display.set_caption('Rabit Hazard') 
    # sprite image
    print 'Stage number is', stage
    if stage == 3:
        stage1.main(screen)

if __name__ == '__main__':
    main()
 
while True:
    input.action()

