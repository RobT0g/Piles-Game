import pygame
from pygame.locals import *


pygame.init()
pxy = [0, 0]    # Mouse position
pos = [0, 0]    # Mouse position relative to the grid


def secl():         # Update and returns mouse position relative to the grid
    global pxy
    pxy = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
    return pxy


def click():        # Detects if I clicked
    return pygame.mouse.get_pressed(num_buttons=3)[0]


def pressesc():     # Detects if I pressed escape
    return pygame.key.get_pressed()[pygame.K_ESCAPE]

