# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
import main

def load_image(name, colorkey=None):
    fullname = os.path.join('data/stage1', name)
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



    
class Map:
    def __init__(self, image, x, y, speed):
        print "Map init"
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.speed = speed

    def render(self, surface):
        surface.blit(self.image, (self.pos_x,self.pos_y))
    

class Player:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.speed = speed
    
        self.soul = 0
    def render(self, surface):
        surface.blit(self.image, (self.pos_x,self.pos_y))


def stage1_main(screen):
    #pygame init
    pygame.init()    

    #player, background image load set
    player_image = load_image("player.bmp").convert_alpha()
    map_image = load_image("background.png").convert_alpha()
    
    #player, background create
    player = Player(player_image, x=0, y=400, speed=1)
    stage_1 = Map(map_image, x=0, y=0, speed=1)
    


    while 1:
        stage_1.render(screen)
        player.render(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if player.pos_x < 0:
            player.pos_x = 0

        pygame.display.update()

    
if __name__ == '__main__':
    main()

