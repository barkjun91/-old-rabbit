# -*- coding: utf-8 -*-

import main
import pygame, sys, os
from pygame.locals import *

SCREEN_SIZE = (800, 600) # screen size set

#load image. where? = main/data/stage1/~
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
    def draw(self, view):
        view.blit(self.image, (self.pos_x,self.pos_y))


class Player:
    def __init__(self, image, x, y, speed):
        self.image = image

	self.margin = 5
	self.jumping_duration = 500
	self.horz_move = speed
	self.time_at_peak = self.jumping_duration / 2
	self.jump_height = 200

        self.pos_x = x
        self.pos_y = y
    	

        self.soul = 0

    def draw(self, view):
        view.blit(self.image, (self.pos_x,self.pos_y))

    def floorY(self, screen):
	return  screen.get_height() - self.image.get_height() - self.margin - 170

    def jumpHeightAtTime(self, elapsedTime):
	return ((-1.0/self.time_at_peak**2)*((elapsedTime-self.time_at_peak)**2)+1)*self.jump_height



def stage1_main(screen):
    #pygame init
    pygame.init()    

    #player, background image load set
    player_image = load_image("player.bmp").convert_alpha()
    map_image = load_image("background.png").convert_alpha()
    
    #player, background create
    player = Player(player_image, x=0, y=400, speed=2)
    stage_1 = Map(map_image, x=0, y=0, speed=1)
    
    jumping = False
    jumpingHorz = 0

    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	
	keys = pygame.key.get_pressed()
        
        def horzMoveAmt():
            ''' Amount of horizontal movement based on left/right arrow keys '''
            return (keys[K_RIGHT] - keys[K_LEFT]) * player.horz_move

        if not jumping:
            player.pos_x += horzMoveAmt()
            if keys[K_SPACE]:
		print "jumpping!"
                jumping = True
                jumpingHorz = horzMoveAmt()
                jumpingStart = pygame.time.get_ticks()

        if jumping:
            t = pygame.time.get_ticks() - jumpingStart
            if t > player.jumping_duration:
                jumping = False
                jumpHeight = 0
            else:
                jumpHeight = player.jumpHeightAtTime(t)
 
            player.pos_y = player.floorY(screen) - jumpHeight
            player.pos_x += jumpingHorz

        if player.pos_x < 0:
            player.pos_x = 0


        stage_1.draw(screen)
        player.draw(screen)
        pygame.display.update()

    
if __name__ == '__main__':
    main()

