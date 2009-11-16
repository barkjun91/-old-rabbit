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

#맵 불러들이기~ 
class Map:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.pos_x = x
        self.pos_y = y
	
        self.speed = speed
    def draw(self, view):
        view.blit(self.image, (self.pos_x,self.pos_y))

#플레이어 로드!
class Player:
    def __init__(self, image, x, y, speed, level):
        self.image = image

	self.margin = 5
	self.jumping_duration = 500
	self.horz_move = speed
	self.time_at_peak = self.jumping_duration / 2
	self.jump_height = 100

	self.we_lev = level 

        self.pos_x = x
        self.pos_y = y
    	

        self.soul = 0

    def draw(self, view):
        view.blit(self.image, (self.pos_x,self.pos_y))

    #착지 Y좌표 찾기~
    def floorY(self, screen):
	return  screen.get_height()-self.image.get_height()-self.margin-130

    #점프에 걸리는 시간 조절(왠만해선 건들지 말것!)
    def jumpHeightAtTime(self, elapsedTime):
	return ((-1.0/self.time_at_peak**2)*((elapsedTime-self.time_at_peak)**2)+1)*self.jump_height

    #공격!
    def attack(self, view, weapon):
	if self.we_lev == 1: #1단계
	    image_att = load_image("attack_"+weapon+"_1.png").convert_alpha()
 	    view.blit(image_att, (self.pos_x, self.pos_y))

	elif self.we_lev == 2: #2단계
	    image_att = load_image("attack_"+weapon+"_2.png").convert_alpha()
 	    view.blit(image_att, (self.pos_x, self.pos_y))	

	elif self.we_lev == 3: #3단계
	    image_att = load_image("attack_"+weapon+"_3.png").convert_alpha()
 	    view.blit(image_att, (self.pos_x, self.pos_y))

	elif self.we_lev == 4: #4단계
	    image_att = load_image("attack_"+weapon+"_4.png").convert_alpha()
 	    view.blit(image_att, (self.pos_x, self.pos_y))

	else:
   	    image_att = load_image("attack_"+weapon+"_1.png").convert_alpha()
 	    view.blit(image_att, (self.pos_x, self.pos_y))
    def skill(self, view, weapon):
	print "스킬발동!"
	

def stage1_main(screen, weapon_type):
    #pygame init
    pygame.init()    

    #player, background image load set
    player_image = load_image("player.bmp").convert_alpha()
    map_image = load_image("background.png").convert_alpha()
    
    #player, background create
    	#플레이어 기본 이미지, 시작 좌표, 기본 이속, 기본 무기 레벨
    player = Player(player_image, x=0, y=440, speed=2, level=1)
	#맵 기본 이미지, 시작 좌표, 맵 이동속도
    stage_1 = Map(map_image, x=0, y=0, speed=1)
    
    jumping = False
    jumpingHorz = 0

    while 1:

        stage_1.draw(screen)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	
	keys = pygame.key.get_pressed()

        # 점프했을때 키보드 오른쪽 혹은 왼쪽 버튼을 눌렀는지 식별 
        def horzMoveAmt():
            ''' Amount of horizontal movement based on left/right arrow keys '''
            return (keys[K_RIGHT] - keys[K_LEFT]) * player.horz_move

	# 점프 했나요?
        if not jumping:
            player.pos_x += horzMoveAmt()
            if keys[K_SPACE]:
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

	# 공격 했나요?
	if keys[K_z]:
	    player.attack(screen, weapon_type)
	else:
            player.draw(screen)

        if player.pos_x < 0:
            player.pos_x = 0



        pygame.display.update()

    
if __name__ == '__main__':
    main()

