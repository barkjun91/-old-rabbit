# -*- coding:utf-8 -

import pygame, sys, os
from pygame.locals import *
import app

class Base(object):
    def __init__(self, image, x, y, speed):
        print "base init"
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.speed = speed

    def render(self, surface):
        surface.blit(self.image, (self.pos_x,self.pos_y))
    

class Stage(Base):
    def __init__(self, image, x, y, speed):
        print "Stage init"
        Base.__init__(self, image, x, y, speed)

class Player(Base):
    def __init__(self, image, x, y, speed):
        print "player init"
        Base.__init__(self, image, x, y, speed)
        self.soul = 0

def main():
    SCREEN_SIZE = (460, 320) # screen size set
    
    #pygame init
    pygame.init()
    
    #screen seting
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    
    #player, background image load set
    player_image = app.load_image("player.bmp").convert_alpha()
    stage_image = app.load_image("background.png").convert_alpha()
    
    #player, background create
    player = Player(player_image, 0, 0, 1)
    stage_1 = Stage(stage_image, 0, 0, 1)
    
    #title set
    pygame.display.set_caption('Rabit Hazard')

    while 1:
        stage_1.render(screen)
        player.render(screen)
        for event in pygame.event.get():
            print event
            if event.type == QUIT:
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

        player.pos_x+= move_x
        player.pos_y-= move_y    

        pygame.display.update()

    
if __name__ == '__main__':
    main()

