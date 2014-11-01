# -*- coding: utf-8 -*-
__author__ = 'clopez'
# http://www.codeskulptor.org/
# OOP-Memory
# 20141028

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    from random import shuffle

width = 800
height = 100
moves = 0
state = 0
first = 0
second = 0
cdeck = []


class Card:
    def __init__(self, value, xpos):
        self.value = value
        self.xpos = xpos
        self.exposed = False
        self.matched = False
        self.width = 50

    def __str__(self):
        s = "Value: " + str(self.value)
        s += " Xpos: " + str(self.xpos)
        s += " Width: " + str(self.width)
        s += " Exposed: " + str(self.exposed)
        return s

    def flip(self):
        if not self.exposed and not self.matched:
            self.exposed = True


def new_game():
    global moves, state, first, second, deck, cdeck
    moves = 0
    state = 0
    first = 0
    second = 0
    deck = range(1, 9) * 2
    shuffle(deck)
    xgrid = range(0, 800, 50)
    cdeck = []
    for d in range(len(deck)):
        cdeck.append(Card(deck[d], xgrid[d]))
    for c in cdeck:
        print str(c)


def draw(canvas):
    i = 8
    for card in cdeck:
        if card.exposed:
            canvas.draw_text(str(card.value), (i, 72), 72, "White", "sans-serif")
        else:
            canvas.draw_polygon([(card.xpos, 0), (card.xpos + card.width, 0), (card.xpos + card.width, height),
                                 (card.xpos, height)], 2, "Green", "Lime")
        i += 50
    lbl.set_text("Moves: " + str(moves))


def click(pos):
    # FIXME: Second click is wrong; especially when card.matched.
    global state, moves, first, second
    x = list(pos)[0]
    print x
    t = x // 50
    if not cdeck[t].exposed and state == 0:
        first = cdeck[t]
        first.exposed = True
        moves += 1
        state = 1
    elif not cdeck[t].exposed and state == 1:
        second = cdeck[t]
        second.exposed = True
        moves += 1
        if second.value == first.value:
            print "Match"
            first.matched = True
            second.matched = True
            #state = 0
        state = 2
    elif state == 2:
        #if first.matched and second.matched:
        #    state = 0
        #else:
        if not first.matched and not second.matched:
            first.exposed = False
            second.exposed = False
        moves += 1
        state = 0


frame = simplegui.create_frame("Memory", width, height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
lbl = frame.add_label("Moves: " + str(moves))
btn = frame.add_button("New game", new_game)
new_game()
frame.start()
