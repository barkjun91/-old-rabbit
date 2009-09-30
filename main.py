# -*- coding:utf-8 -*-

import pygame, sys,os
from pygame.locals import * 
import app
import stage1


#stage = ["title", "main", "stage1"]
stage = 1

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def main():
    SCREEN_SIZE = (460, 320) # screen size set
    # Start up pygame/make screen
    pygame.init() 

    #screen seting
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    
    #title set
    pygame.display.set_caption('Rabit Hazard') 
    
    print 'Stage number is', stage

    #call stage1.main
    if stage == 1:
        stage1.stage1_main(screen)

if __name__ == '__main__':
    main()
 

