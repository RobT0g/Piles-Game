import InputManager

piles = [[6, 5, 4, 3, 2, 1], [], []]
pile1 = piles[0]                # Pile 1
pile2 = piles[1]                # Pile 2
pile3 = piles[2]                # Pile 3
piletop = []
bottom = 345
heights = [bottom, (bottom-22), (bottom-44), (bottom-66), (bottom-88), (bottom-112)]
pxy = []
moving = 4


def setpiletop():
    global piletop, pile1, pile2, pile3
    piletop = [0, 0, 0]
    piletop[0] = len(pile1) - 1
    piletop[1] = len(pile2) - 1
    piletop[2] = len(pile3) - 1


def getpiletop():
    global piletop
    setpiletop()
    return piletop


def xclickbox(p):
    xcbox = [21 + 4 * (6-p), 179 - 4 * (6-p)]
    return xcbox


def clickedat():
    global pxy, piletop, moving
    pxy = InputManager.secl()
    setpiletop()
    pt = [0, 0, 0]
    if pile1:
        pt[0] = pile1[piletop[0]]
        if pxy[0] in range(xclickbox(pt[0])[0], xclickbox(pt[0])[1]):
            if pxy[1] in range(heights[piletop[0]], heights[piletop[0]] + 44):
                moving = 0
                return [pxy, 0]
    if pile2:
        pt[1] = pile2[piletop[1]]
        if pxy[0] in range(xclickbox(pt[1])[0]+200, xclickbox(pt[1])[1]+200):
            if pxy[1] in range(heights[piletop[1]], heights[piletop[1]] + 44):
                moving = 1
                return [pxy, 1]
    if pile3:
        pt[2] = pile3[piletop[2]]
        if pxy[0] in range(xclickbox(pt[2])[0]+400, xclickbox(pt[2])[1]+400):
            if pxy[1] in range(heights[piletop[2]], heights[piletop[2]] + 44):
                moving = 2
                return [pxy, 2]


def getpiles():
    global piles
    return piles


def setpiles(pos):
    global moving, piles
    stopedat = []
    if pos[1] > 120:
        if pos[0] + 50 in range(65, 85):
            stopedat = [0]
        elif pos[0] + 50 in range(265, 285):
            stopedat = [1]
        elif pos[0] + 50 in range(465, 485):
            stopedat = [2]
    if stopedat and moving != 4:
        if piles[moving]:
            if piles[stopedat[0]]:
                if piles[moving][-1] < piles[stopedat[0]][-1]:
                    piles[stopedat[0]].append(piles[moving][-1])
                    piles[moving].pop()
            else:
                piles[stopedat[0]].append(piles[moving][-1])
                piles[moving].pop()
