# -*- coding: utf-8 -*-
__author__ = 'clopez'
# Memory. Now for real.
# 20141028

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    from random import shuffle

width = 800
height = 100

deck = range(1, 9) * 2
shuffle(deck)
xgrid = range(0, 800, 50)
exposed = [False] * len(deck)
moves = 0
state = 0

#bigone = [(x, y, z) for x in deck for y in xgrid for z in exposed]
bigone = zip(deck, xgrid)
#bigone[0][2] = True


print deck
print xgrid
print exposed


def new_game():
    global deck, exposed, moves, state
    deck = range(1, 9) * 2
    shuffle(deck)
    exposed = [False] * len(deck)
    moves = 0
    state = 0


def draw(canvas):
    i = 8
    for card in range(len(deck)):
        if exposed[card]:
            canvas.draw_text(str(deck[card]), (i, 72), 72, "White", "sans-serif")
        else:
            canvas.draw_polygon([(xgrid[card], 0), (xgrid[card] + 50, 0), (xgrid[card] + 50, height), (xgrid[card], height)], 2, "Green", "Lime")
        i += 50
    lbl.set_text("Moves: " + str(moves))


def click(pos):
    global moves, state
    xpos = list(pos)[0]
    print xpos
    first = 0
    second = 0

    for hor in range(len(xgrid)):
        if xgrid[hor] <= xpos < (xgrid[hor] + 50) and not exposed[hor] and state == 0:
            exposed[hor] = True
            first = hor
            print "Flipped card " + str(hor)
            print exposed
            state = 1
            moves += 1
        elif xgrid[hor] <= xpos < (xgrid[hor] + 50) and not exposed[hor] and state == 1:
            exposed[hor] = True
            second = hor
            print "Flipped card " + str(hor)
            print exposed
            state = 2
            moves += 1
        elif state == 2:
            exposed[first] = False
            exposed[second] = False
            exposed[hor] = True
            first = hor
            print "Flipped card " + str(hor)
            print exposed
            state = 1
            moves += 1


frame = simplegui.create_frame("Memory", width, height)
lbl = frame.add_label("Moves: " + str(moves))
btn = frame.add_button("New game", new_game)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()