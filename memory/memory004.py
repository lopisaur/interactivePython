# -*- coding: utf-8 -*-
__author__ = 'clopez'
# http://www.codeskulptor.org/
# "Memory" - Assignment x
# 20141025

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
#exposed = [True] * len(deck)
#exposed[3] = True
#exposed[7] = True

moves = 0
state = 0

print deck
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



def mouseclick(pos):
    global moves, state
    x = list(pos)[0]
    print x
    print "x//50 = " + str(x//50)
    t = x // 50
    first = 0
    second = 0

    #if state == 0 and not exposed[t]:
    #    first = t
    #    exposed[first] = True
    #    moves += 1
    #    state = 1
    #if state == 1 and not exposed[t]:
    #    second = t
    #    exposed[second] = True
    #    moves += 1
    #    if deck[first] != deck[second]:
    #        exposed[first] = False
    #        exposed[second] = False
    #        first = 0
    #        second = 0
    #        state = 0
    #    else:
    #        state = 2
    #if state == 2:
    #    exposed[first] = False
    #    exposed[second] = False
    #if not exposed[t]:
    #moves += 1
    #if state == 0:
    #    first = t
    #    state = 1
    #    exposed[first] = True
    #    print deck[first]
    #elif state == 1:
    #    second = t
    #    state == 2
    #    exposed[second] = True
    #    print deck[first]
    #    print deck[second]
    ##else:
    #    if deck[first] == deck[second]:
    #        exposed[first] = True
    #        exposed[second] = True
    #        print "x"
    #else:
    #    exposed[first] = False
    #    exposed[second] = False
    #    state = 1
    #    print deck[first]
    #    print deck[second]
    #    first = 0
    #    second = 0

    #for i in range(len(xgrid)):
    #    if xgrid[i] <= x < xgrid[i] + 50 and not exposed[i]:
    #        print xgrid[i], i
    #        print "Hit card " + str(deck[i])
    #        exposed[i] = True
    #for i in range(len(deck)):
    #    if not exposed[t]:
    #        exposed[t] = True
#    if not exposed[t]:
#        moves += 1
#        if state == 0:
#            first = t
#            exposed[t] = True
#            state = 1
#        elif state == 1:
#            second = t
#            exposed[t] = True
#            if deck[first] == deck[second]:
#                deck.pop(first)
#                deck.pop(second)
#                exposed.pop(first)
#                exposed.pop(second)
#                state = 0
#            else:
#                state = 2
#        else:
#            exposed[first] = False
#            exposed[second] = False
#            state = 1
    if not exposed[t] and state == 0:
        moves += 1
        first = t
        exposed[first] = True
        state = 1
    elif state == 1:
        moves += 1
        second = t
        exposed[second] = True
        if deck[first] == deck[second]:
            #deck.pop(first)
            #deck.pop(second)
            state = 0
        else:
            state = 2
    else:
        exposed[first] = False
        exposed[second] = False
        state = 1
    #




frame = simplegui.create_frame("Memory", width, height)
lbl = frame.add_label("Moves: " + str(moves))
btn = frame.add_button("New game", new_game)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

frame.start()