import pygame

import InputManager
import PositionsManager

pile1 = [6, 5, 4, 3, 2, 1]  # Pile 1
pile2 = []  # Pile 2
pile3 = []  # Pile 3

background = pygame.image.load('images/Base.png')   # Background
backpiles = pygame.image.load('images/Piles.png')   # Piles

# pieces
piece1 = pygame.image.load('images/Piece1.png')
piece1b = pygame.image.load('images/Piece1bg.png')
piece2 = pygame.image.load('images/Piece2.png')
piece2b = pygame.image.load('images/Piece2bg.png')
piece3 = pygame.image.load('images/Piece3.png')
piece3b = pygame.image.load('images/Piece3bg.png')
piece4 = pygame.image.load('images/Piece4.png')
piece4b = pygame.image.load('images/Piece4bg.png')
piece5 = pygame.image.load('images/Piece5.png')
piece5b = pygame.image.load('images/Piece5bg.png')
piece6 = pygame.image.load('images/Piece6.png')
piece6b = pygame.image.load('images/Piece6bg.png')

# Line for reference
refeline = pygame.image.load('images/ReferLine.png')

# Default Positions
bottom = 345
widths = [25, 225, 425]
heights = [bottom, (bottom - 22), (bottom - 44), (bottom - 66), (bottom - 88), (bottom - 112)]
instwidths = widths[:]
instheights = heights[:]

drag = False  # This defines if the code is meant to drag a piece
dragp = [[], 0]  # This gives the info on what piece the code is dragging
pos = []  # This is the current mouse position
piletop = [5, 0, 0]  # This register the index of the piece on the top of the list
dist = []
sdist = []


def initialize(screen):
    setonscreen(screen)


def setonscreen(screen):
    global pile1, pile2, pile3, widths, heights, instwidths, instheights, piletop, dragp
    screen.blit(background, (0, 0))
    for k, v in enumerate(pile1):
        if v != 0 and k != piletop[0]:
            setpieceb(screen, v, widths[0], heights[k])
        elif k == piletop[0]:
            if dragp[1] == 0:
                setpieceb(screen, v, instwidths[0], instheights[k])
            else:
                setpieceb(screen, v, widths[0], heights[k])
    for k, v in enumerate(pile2):
        if v != 0 and k != piletop[1]:
            setpieceb(screen, v, widths[1], heights[k])
        elif k == piletop[1]:
            if dragp[1] == 1:
                setpieceb(screen, v, instwidths[1], instheights[k])
            else:
                setpieceb(screen, v, widths[1], heights[k])
    for k, v in enumerate(pile3):
        if v != 0 and k != piletop[2]:
            setpieceb(screen, v, widths[2], heights[k])
        elif k == piletop[2]:
            if dragp[1] == 2:
                setpieceb(screen, v, instwidths[2], instheights[k])
            else:
                setpieceb(screen, v, widths[2], heights[k])
    screen.blit(backpiles, (0, 0))
    for k, v in enumerate(pile1):
        if v != 0 and k != piletop[0]:
            setpiece(screen, v, widths[0], heights[k])
        elif k == piletop[0]:
            if dragp[1] == 0:
                setpiece(screen, v, instwidths[0], instheights[k])
            else:
                setpiece(screen, v, widths[0], heights[k])
    for k, v in enumerate(pile2):
        if v != 0 and k != piletop[1]:
            setpiece(screen, v, widths[1], heights[k])
        elif k == piletop[1]:
            if dragp[1] == 1:
                setpiece(screen, v, instwidths[1], instheights[k])
            else:
                setpiece(screen, v, widths[1], heights[k])
    for k, v in enumerate(pile3):
        if v != 0 and k != piletop[2]:
            setpiece(screen, v, widths[2], heights[k])
        elif k == piletop[2]:
            if dragp[1] == 2:
                setpiece(screen, v, instwidths[2], instheights[k])
            else:
                setpiece(screen, v, widths[2], heights[k])


def setpieceb(screen, p, x, y):
    if p == 1:
        screen.blit(piece1b, (x, y))
    elif p == 2:
        screen.blit(piece2b, (x, y))
    elif p == 3:
        screen.blit(piece3b, (x, y))
    elif p == 4:
        screen.blit(piece4b, (x, y))
    elif p == 5:
        screen.blit(piece5b, (x, y))
    elif p == 6:
        screen.blit(piece6b, (x, y))


def setpiece(screen, p, x, y):
    if p == 1:
        screen.blit(piece1, (x, y))
    elif p == 2:
        screen.blit(piece2, (x, y))
    elif p == 3:
        screen.blit(piece3, (x, y))
    elif p == 4:
        screen.blit(piece4, (x, y))
    elif p == 5:
        screen.blit(piece5, (x, y))
    elif p == 6:
        screen.blit(piece6, (x, y))


def update():
    global drag, dragp, pos, widths, heights, instwidths, instheights, piletop, pile1, pile2, pile3, dist, sdist
    piles = [pile1, pile2, pile3]
    piletop = PositionsManager.getpiletop()
    if not drag:
        instwidths = widths[:]
        instheights = heights[:]
        if x := PositionsManager.clickedat():
            drag = True
            dragp = x
    else:
        piecem = piles[dragp[1]][-1]
        pos = InputManager.secl()
        if (r := heights[piletop[dragp[1]]] + (pos[1] - dragp[0][1])) in range(9, bottom):
            instheights[piletop[dragp[1]]] = r
        if (a := widths[dragp[1]] + (pos[0] - dragp[0][0])) in range(9 - (6 - piecem) * 4, 441 + (6 - piecem) * 4):
            if instheights[piletop[dragp[1]]] in range(100, bottom):
                if dist:
                    instwidths[dragp[1]] = widths[dist.index(sdist[0])]
                else:
                    instwidths[dragp[1]] = widths[dragp[1]]
            else:
                dist = [modul(widths[0] - a), modul(widths[1] - a), modul(widths[2] - a)]
                sdist = sorted(dist)
                instwidths[dragp[1]] = a


def reset():
    global drag, instwidths, instheights, piletop, dist, sdist
    drag = False
    PositionsManager.setpiles([instwidths[dragp[1]], instheights[piletop[dragp[1]]]])
    uppiles()
    instwidths = widths[:]
    instheights = heights[:]
    dist = []
    sdist = []


def uppiles():
    global pile1, pile2, pile3
    piles = PositionsManager.getpiles()
    pile1 = piles[0][:]
    pile2 = piles[1][:]
    pile3 = piles[2][:]


def modul(x):
    if x < 0:
        return -x
    return x
