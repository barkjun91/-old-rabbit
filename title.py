# -*- coding:utf-8 -*-

import pygame
import app

def main(screen):
    # Load logo
    logo = app.load_image("player.bmp", -1)
    r = image.get_rect()
    # blit background on to the screen

    # Create a new FaderSurface with the same dimensions and an initial
    # transparency of 1.

    surface = Complex.FaderSurface(r.width, r.height, 1)
    
    #Blit the original o  the FaderSurface.
    screen.blit(logo, (0,0))

    #The default step value is -1, but we wnat to fade the image in.
    surface.step = 1

# Loop until the FaderSurface reached the maximum or minimum alpha
# transparency value.
while surface.update():

    # Clean up and blit the surface..
    screen.fill ((180, 180, 180))
    screen.blit (surface, (10, 10))
    pygame.display.flip ()

    # Check the bounds. We have to check the maximum values - 1, because
    # 255 and 0 cause the surface to return False and we would exit the
    # loop.
    if surface.alpha == 254 or surface.alpha == 1:
        surface.step = -surface.step

    pygame.time.delay (50 / 4)
    
    # Wait for input.
    if pygame.event.get ([pygame.locals.QUIT]):
        break


if __name__ == '__main__':
    main()

