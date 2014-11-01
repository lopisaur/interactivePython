# -*- coding: utf-8 -*-
__autor = "clopez"

try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import shuffle

deck = range(1, 9) + range(1, 9)
shuffle(deck)
xgrid = range(0, 800, 50)

width = 800
height = 100

exposed = False

# (xpos, card)
cl = zip(xgrid, deck)
print cl
cardcoord = []
for card in cl:
    #cardcoord.insert(card[1], [(card[0], 0), (card[0] + 50, 0), (card[0] + 50, height), (card[0], height)])
    cardcoord.append([(card[0], 0), (card[0] + 50, 0), (card[0] + 50, height), (card[0], height)])

print "cardcoord:\n"
print cardcoord

bigone = zip(deck, cardcoord)
print "bigone:\n"
print bigone

newone = zip(cl, [False]*len(cl))
#newone = list(newone)
print "newone:\n"
print newone

newerone = [list(card) for card in newone]
print "newerone\n"
print newerone


def draw(canvas):
    for card in cl:
        if exposed:
            canvas.draw_text(str(card[1]), (card[0] + 8, 72), 72, "White", "sans-serif")
        else:
            canvas.draw_polygon([(card[0], 0), (card[0] + 50, 0), (card[0] + 50, height), (card[0], height)], 2, "Green", "Lime")


def click(pos):
    global exposed
    pos = list(pos)
    print pos[0]
    #for d in cl:
    #    x = pos[0]
    #    if x > d[0] and x < d[0] + 50:
    #        exposed = True
    #        print str(d[1])
    #for e in newone:
    #    #print e
    #    #print e[0][0]
    #    x = pos[0]
    #    if x > e[0][0] and x < e[0][0] + 50:
    #        print "Hit card" + str(e[0][1])
    #        #e[1] = True
    #        print str(e[1])
    #        print e
    #        print type(e)
    #        print type(e[1])
    for e in newerone:
        x = pos[0]
        if x > e[0][0] and x < e[0][0] + 50:
            print "Hit card " + str(e[0][1])
            e[1] = True
            print str(e[1])
            print e
            print type(e)
            print type(e[1])


frame = simplegui.create_frame("Memory", width, height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()
