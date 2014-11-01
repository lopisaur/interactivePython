__author__ = 'clopez'
# http://www.codeskulptor.org/
# "xxx" - Assignment 3
# 20141024

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import shuffle

xgrid = range(0, 800, 50)  # x-Axis coordinates
deck = range(1, 9) + range(1, 9)
shuffle(deck)
cl = zip(deck, xgrid)

print xgrid
print cl

print(cl[0][0], (cl[0][1], 50), 24, "White")

#for card, xcoord in cl:
#    print(card, (xcoord, 50), 24, "White")

# helper function to initialize globals
#def new_game():
#    pass


# define event handlers
#def mouseclick(pos):
#    # add game state logic here
#    pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    # Card printing:
    for card, xcoord in cl:
        canvas.draw_text(str(card), (xcoord, 75), 72, "White", "sans-serif")
    for x in xgrid:
        canvas.draw_line((x, 0), (x, 100), 1, "Green")
    # First polygon - OK:
    # canvas.draw_polygon([(xgrid[0], 0), (xgrid[1], 0), (xgrid[1], 100), (xgrid[0], 100)], 2, "Green", "Lime")
    #i = 0
    #while i < len(xgrid) - 1:
    #    global i
    #    print (xgrid[i], xgrid[i + 1], xgrid[i + 1], xgrid[i])
    #    canvas.draw_polygon([(xgrid[i], 0), (xgrid[i + 1], 0), (xgrid[i + 1], 100), (xgrid[i], 100)], 2, "Green", "Lime")
    #    i += 1




# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
#frame.add_button("Reset", new_game)
#label = frame.add_label("Turns = 0")

# register event handlers
#frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
#new_game()
frame.start()


# Always remember to review the grading rubric