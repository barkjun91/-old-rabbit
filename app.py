import pygame, sys,os
from pygame.locals import * 

pygame.init() 


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

 
def input(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
      elif event.type == KEYDOWN: 
         print event 
      else:
         print 'asdf'
