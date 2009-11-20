#-*- coding:utf-8 -*-

import pygame, sys,os
from pygame.locals import * 
import stage1


#stage = ["title", "main", "stage1"]
stage = 1


def main():
    SCREEN_SIZE = (800, 600) # screen size set
    # Start up pygame/make screen
    pygame.init() 

    #screen seting
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    
    #title set
    pygame.display.set_caption('Rabbit Hazard') 
    weapon_type = "gun"
    game_status = True
    #call stage1.main
    while game_status:
    	if stage == 1:
           game_status = stage1.stage1_main(screen, weapon_type)


if __name__ == '__main__':
    main()
 

