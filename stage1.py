# -*- coding:utf-8 -

SCREEN_SIZE = (460, 320)
PLAYER_X=0
PLAYER_Y=0
import pygame, sys, os
from pygame.locals import *
import app

class Base(object):
    def __init__(self, image):
        print "base init"
        self.image = image

    def render(self, surface):

        surface.blit(self.image, (PLAYER_X,PLAYER_Y))
        
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
    player = Player(player_image)
    pygame.display.set_caption('Rabit Hazard') 

    while 1:
        player.render(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_x = -1
                elif event.key == K_RIGHT:
                    move_x = +1
                elif event.key == K_UP:
                    move_y = +1
                elif event.key == K_DOWN:
                    move_y = -1
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    move_x = 0
                elif event.key == K_RIGHT:
                    move_x = 0
                elif event.key == K_UP:
                    move_y = 0
                elif event.key == K_DOWN:         
                    move_y = 0
        PLAYER_X+= move_x
        PLAYER_Y-= move_y    

        pygame.display.update()

    
if __name__ == '__main__':
    main()

