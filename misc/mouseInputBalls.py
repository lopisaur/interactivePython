__author__ = 'clopez'
# http://www.codeskulptor.org/
# Mouse input, balls & lists
# 20141020

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Indigo"

def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def click(pos):
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            remove.append(ball)
    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle((ball[0], ball[1]), ball_radius, 1, "Black", ball_color)

frame = simplegui.create_frame("The balls", width, height)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.start()