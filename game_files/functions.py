import os
import pygame
from pygame.locals import *

def load_image(file_name, colorkey=None,size=None):
    full_name = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data', file_name)

    try:
        image = pygame.image.load(full_name)
    except pygame.error as message:
        print('Cannot load image: ', full_name)
        raise SystemExit(message)

    image = image.convert()
    if size != None:
        image=pygame.transform.scale(image,size)

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def get_key(event, player):
    # print event
    if event.type == pygame.QUIT: pygame.quit()

    left,right = player.velocity[0]
    up,down = player.velocity[1]
    if event.type == KEYDOWN:
        if event.key == K_UP:
            up = 4
        if event.key == K_DOWN:
            down = -4
        if event.key == K_LEFT:
            left = 4
        if event.key == K_RIGHT:
            right = -4
        if event.key == K_LCTRL or event.key == K_RCTRL:
            player.create_attack([0, -3])

    if event.type == KEYUP:
        if event.key == K_LEFT:
            left = 0
        if event.key == K_UP:
            up = 0
        if event.key == K_DOWN:
            down = 0
        if event.key == K_RIGHT:
            right = 0

    player.velocity = [[left,right], [up,down]]
