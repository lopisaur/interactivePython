__author__ = 'clopez'
# http://www.codeskulptor.org/
# "Memory" - Assignment 5
# 20141023

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

deck = range(9) + range(9)
random.shuffle(deck)
print(deck)
for card in deck:
    print card


# helper function to initialize globals
#def new_game():
#    pass


# define event handlers
#def mouseclick(pos):
#    # add game state logic here
#    pass


# cards are logically 50x100 pixels in size
#def draw(canvas):
#    pass


# create frame and add a button and labels
#frame = simplegui.create_frame("Memory", 800, 100)
#frame.add_button("Reset", new_game)
#label = frame.add_label("Turns = 0")

# register event handlers
#frame.set_mouseclick_handler(mouseclick)
#frame.set_draw_handler(draw)

# get things rolling
#new_game()
#frame.start()


# Always remember to review the grading rubric
