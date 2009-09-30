# -*- coding:utf-8 -

SCREEN_SIZE = (460, 320)
PLAYER_X=0
PLAYER_Y=250
import pygame, sys, os
from pygame.locals import *
import app

class Base(object):
    def __init__(self, image):
        print "base init"
        self.image = image
    def render(self, surface, x, y):
        surface.blit(self.image, (x,y))

class Stage(Base):
    def __init__(self, image):
        Base.__init__(self, image)

class Player(Base):
    def __init__(self, image):
        print "player init"
        Base.__init__(self, image)

def main():
    global PLAYER_X
    global PLAYER_Y
    move_x, move_y = 0, 0
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    player_image = app.load_image("player.bmp").convert_alpha()
    stage_image = app.load_image("background.png").convert_alpha()
    player = Player(player_image)
    stage = Stage(stage_image)
    pygame.display.set_caption('Rabit Hazard') 
    stage.render(screen, 0, 0)
    while 1:
        player.render(screen, PLAYER_X, PLAYER_Y)
        for event in pygame.event.get():
            print event
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT and not(event.key == K_RIGHT):
                    move_x = -1
                elif event.key == K_RIGHT and not(event.key == K_LEFT):
                    move_x = +1
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    move_x = 0
                elif event.key == K_RIGHT:
                    move_x = 0
        PLAYER_X+= move_x
        PLAYER_Y-= move_y    

        pygame.display.update()

    
if __name__ == '__main__':
    main()

