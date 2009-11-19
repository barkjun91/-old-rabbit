# -*- coding: utf-8 -*-

import main
import pygame, sys, os, random
from pygame.locals import *

SCREEN_SIZE = (800, 600) # screen size set

# define where to get the tile image form in the tiles source image
tile_coords = {
    'a': (0,0), # noraml_ground
    'b': (80,0), # up_ground
    'c': (160,0), # down_ground
    '.': None,
}

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
    def __init__(self, map, tiles):
	self.tiles = load_image(tiles)	
	self.width = 0
	l = [line.strip() for line in open('data/stage1/' + map).readlines()]
	self.map = [[None]*len(l[0]) for j in range(len(l))]
	
	for i in range(len(l[0])):
	    self.width += 80
	    for j in range(len(l)):
		tile = l[j][i]
		tile = tile_coords[tile]
		if tile is None:
		    continue
                elif isinstance(tile, type([])):
                    tile = random.choice(tile)
		cx, cy = tile
		self.map[j][i] = (cx, cy)
    def limt(self, object):
        if object.pos_x < 0:
            object.pos_x = 0
	elif object.pos_x > 770:
	    object.pos_x = 770

    def draw(self, view, viewpos):
	sx, sy = view.get_size()
	bx = viewpos[0]/80 
	by = viewpos[1]/80
	for x in range(0, sx+80, 80):
	    i = x/80 + bx
	    for y in range(0, sy+80, 80):
		j = y/80 + by
		try:
		    tile = self.map[j][i]
		except IndexError:
		    continue
		if tile is None:
		    continue
		cx, cy = tile
		view.blit(self.tiles, (x, y), (cx, cy, 80, 80))

class Player:
    def __init__(self, image, playerpos, speed, level):
        self.image = image

	self.margin = 5
	self.jumping_duration = 500
	self.horz_move = speed
	self.time_at_peak = self.jumping_duration / 2
	self.jump_height = 100

	self.we_lev = level 

        self.pos_x, self.pos_y = playerpos
    	

        self.soul = 0

    def draw(self, view):
        view.blit(self.image, (self.pos_x, self.pos_y))

    #착지 Y좌표 찾기~
    def floorY(self, screen):
	return  screen.get_height()-self.image.get_height()-self.margin-130

    #점프에 걸리는 시간 조절(왠만해선 건들지 말것!)
    def jumpHeightAtTime(self, elapsedTime):
	return ((-1.0/self.time_at_peak**2)*((elapsedTime-self.time_at_peak)**2)+1)*self.jump_height


def stage1_main(screen, weapon_type):
    #pygame init
    pygame.init()    

    #player, background image load set
    player_image = load_image("player.bmp").convert_alpha()
    map_image = load_image("background.png").convert_alpha()
    map = Map('map.txt', 'tiles.png')
    viewpos = (0,0)
    playerpos = (0, 440) 
    #player, background create
    	#플레이어 기본 이미지, 시작 좌표, 기본 이속, 기본 무기 레벨
    player = Player(player_image, playerpos, speed=2, level=1)
    
    jumping = False
    jumpingHorz = 0

    while 1:
	screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	playerpos = (player.pos_x, player.pos_y)
	keys = pygame.key.get_pressed()

	#좌우로 움직이기
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

        player.draw(screen)
	
	map.limt(player)	
	print playerpos
	map.draw(screen, viewpos)
        pygame.display.update()

    
if __name__ == '__main__':
    main()

