import pygame
from pygame.locals import *
import InputManager
import ScreenManager
import PositionsManager

pygame.init()

screen_width = 600                                                      # Screen width
screen_height = 400                                                     # Screen Height

screen = pygame.display.set_mode((screen_width, screen_height))         # Screen defined
pygame.display.set_caption('Pile')                                      # Screen name

running = True                          # Flux variable
ScreenManager.initialize(screen)        # This makes the base screen appear at first
pygame.display.flip()                   # This make the screen update (show on screen)
refresh = False

while running:
    # looping
    for event in pygame.event.get():
        if InputManager.pressesc():     # If I press escape:
            running = False
        if pygame.mouse.get_pressed()[0]:
            # This is where everything is going to happen
            try:
                ScreenManager.update()              # That's going to make the game update itself
                ScreenManager.setonscreen(screen)   # Put stuff on screen
                pygame.display.flip()               # Update the screen
                refresh = True
            except AttributeError:
                pass
        if refresh:
            if not pygame.mouse.get_pressed()[0]:
                ScreenManager.reset()                   # Reset the positions
                ScreenManager.setonscreen(screen)       # Put stuff on screen
                pygame.display.flip()                   # Update the screen
                refresh = False
