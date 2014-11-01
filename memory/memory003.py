# -*- coding: utf-8 -*-
__author__ = 'clopez'
# http://www.codeskulptor.org/
# "Memory" - Assignment 5
# 20141025

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import shuffle

deck = range(1, 9) * 2
shuffle(deck)
xgrid = range(0, 800, 50)

width = 800
height = 100

expcards = 0


# carddeck: [x-coordinate, value, exposed]
# Make a list of lists containing the card's horizontal starting coordinate, value and "expose" flag.
# List comprehension necessary to convert zip's tuples to lists.
carddeck = [list(card) for card in zip(xgrid, deck, [False] * len(deck))]
print carddeck


def new_game():
    global deck, xgrid, carddeck
    deck = range(1, 9) * 2
    shuffle(deck)
    xgrid = range(0, 800, 50)
    carddeck = [list(card) for card in zip(xgrid, deck, [False] * len(deck))]
    print carddeck


def draw(canvas):
    for c in carddeck:
        if c[2]:
            canvas.draw_text(str(c[1]), (c[0] + 8, 72), 72, "White", "sans-serif")
        else:
            canvas.draw_polygon([(c[0], 0), (c[0] + 50, 0), (c[0] + 50, height), (c[0], height)], 2, "Green", "Lime")
#def click(pos):
#    remove = []
#    for ball in ball_list:
#        if distance(ball, pos) < ball_radius:
#            remove.append(ball)
#    if remove == []:
#        ball_list.append(pos)
#    else:
#        for ball in remove:
#            ball_list.pop(ball_list.index(ball))

def click(pos):
    global expcards
    pos = list(pos)
    for point in carddeck:
        x = pos[0]
        if point[0] <= x < point[0] + 50:
            print x, "Card: " + str(point[1])
            point[2] = True
            expcards += 1
    print "Cards showing: " + str(expcards)

frame = simplegui.create_frame("Memory", width, height)
btn1 = frame.add_button("New game", new_game, 200)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()