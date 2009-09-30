# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *
import main
class Base():
    def __init__(self, image, x, y, speed):
        print "base init"
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.speed = speed
    
    def render(self, surface):
        surface.blit(self.image, (self.pos_x,self.pos_y))
    
class Map(Base):
    def __init__(self, image, x, y, speed):
        print "Map init"
        Base.__init__(self, image, x, y, speed)

class Player(Base):
    def __init__(self, image, x, y, speed):
        print "player init"
        Base.__init__(self, image, x, y, speed)
        self.soul = 0


def stage1_main(screen):
    #pygame init
    pygame.init()    

    #?
    move_x, move_y = 0, 0

    #player, background image load set
    player_image = main.load_image("player.bmp").convert_alpha()
    map_image = main.load_image("background.png").convert_alpha()
    
    #player, background create
    player = Player(player_image, x=0, y=260, speed=1)
    stage_1 = Map(map_image, x=0, y=0, speed=1)
    


    while 1:
        stage_1.render(screen)
        player.render(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = -player.speed
                elif event.key == K_RIGHT:
                    move_x = +player.speed
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    move_x = 0
                elif event.key == K_RIGHT:
                    move_x = 0
        
        if player.pos_x < 0:
            player.pos_x = 0

        player.pos_x+= move_x
        player.pos_y-= move_y    

        pygame.display.update()

    
if __name__ == '__main__':
    main()

