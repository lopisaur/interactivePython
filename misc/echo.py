__author__ = 'clopez'
# echo
# 20141014

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

current_key = " "


def keydown(key):
    global current_key
    current_key = chr(key)


def keyup(key):
    global current_key
    current_key = " "


def draw(canvas):
    canvas.draw_text(current_key, [10, 25], 20, "Red")

frame = simplegui.create_frame("Echo", 35, 35)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

frame.start()