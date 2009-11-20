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

    def draw(self, view, viewpos, camera):
	sx, sy = (self.width, 600)
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
		view.blit(self.tiles, (x-camera.px, y-camera.py), (cx, cy, 80, 80))

class Camera:
    def __init__(self, view):
	x, y = view.get_size()
	self.view_posx, self.view_posy = (x/2, y/2)
	self.px, self.py = (0,0)
  

class Player:
    def __init__(self, image, playerpos, speed, level):
        self.image = image

	self.margin = 5
	self.jumping_duration = 500
	self.speed = speed
	self.time_at_peak = self.jumping_duration / 2
	self.jump_height = 100
	self.we_lev = level 
        self.pos_x, self.pos_y = playerpos
        self.soul = 0



    #착지 Y좌표 찾기~
    def floorY(self, screen):
	return  screen.get_height()-self.image.get_height()-self.margin-130

    #점프에 걸리는 시간 조절(왠만해선 건들지 말것!)
    def jumpHeightAtTime(self, elapsedTime):
	return ((-1.0/self.time_at_peak**2)*((elapsedTime-self.time_at_peak)**2)+1)*self.jump_height

    def horzMoveAmt(self, keys, object):
        return (keys[K_RIGHT] - keys[K_LEFT]) * object.speed

    def draw(self, view):
        view.blit(self.image, (self.pos_x, self.pos_y))


def stage1_main(screen, weapon_type):
    pygame.init()
    viewpos = (0,0)
    playerpos = (0, 440)
    jumping = False
    jumpingHorz = 0
    game_status = True

# --------------------- image load ---------------------------- 
    player_image = load_image("player.bmp").convert_alpha()
    map_image = load_image("background.png").convert_alpha()

# ------------------- Create Object ---------------------------- 
    player = Player(player_image, playerpos, speed=2, level=1)
    map = Map('map.txt', 'tiles.png')
    camera = Camera(screen)

# -------------------- Start Game -----------------------------    
    while game_status:
	screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
	keys = pygame.key.get_pressed()
    # ------------------------ player move ------------------
        if not jumping:
	    if player.pos_x < camera.view_posx or camera.px < 0:
		print "a"
	 	player.pos_x += player.horzMoveAmt(keys, player)
		if camera.px < 0:
		    camera.px = 0
	    if camera.view_posx <= camera.px+player.pos_x <= map.width-camera.view_posx:
		print "b"
		if player.pos_x < 400:
		    player.pos_x = 400
		camera.px += player.horzMoveAmt(keys, player)
	    if map.width-camera.view_posx < camera.view_posx + camera.px:
		print "c"
		player.pos_x += player.horzMoveAmt(keys, player)

            if keys[K_SPACE]:
                jumping = True
                jumpingHorz = player.horzMoveAmt(keys, player)
                jumpingStart = pygame.time.get_ticks()
    # ---------------------- jumping -----------------------

        if jumping:
            t = pygame.time.get_ticks() - jumpingStart
            if t > player.jumping_duration:
                jumping = False
                jumpHeight = 0
            else:
                jumpHeight = player.jumpHeightAtTime(t)
 
            player.pos_y = player.floorY(screen) - jumpHeight
	    if player.pos_x < camera.view_posx or camera.px < 0:
	        player.pos_x += jumpingHorz
	    else:
		camera.px += jumpingHorz

# -------------------------------------------------------
	map.limt(player)
# ------------------------ Drawing ----------------------	
        player.draw(screen)
	map.draw(screen, viewpos, camera)
        pygame.display.update()
# -------------------------------------------------------
    
if __name__ == '__main__':
    main()

