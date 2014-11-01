__author__ = 'clopez'
# Random ball with collision/reflection
# 20141015

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange


width = 600
height = 400
radius = 20

pos = [width / 2, height / 2]
#vel = [1, 3]
vel = [randrange(-8, 9), randrange(-8, 9)]

print (vel)


def draw(canvas):
    global pos, vel
    pos[0] += vel[0]
    pos[1] += vel[1]
    canvas.draw_circle(pos, radius, 2, "White", "Blue")
    if pos[0] < radius or pos[0] > (width - 1) - radius:
        print "horizontal collision"
        #pos = [width / 2, height / 2]
        vel[0] = -vel[0]
        #if vel[0] < 0:
        #    vel[0] = randrange(0, 9)
        #else:
        #    vel[0] = randrange(-8, 0)
    if pos[1] < radius or pos[1] > (height - 1) - radius:
        print "vertical collision"
        #pos = [width / 2, height / 2]
        vel[1] = -vel[1]
        #if vel[1] < 0:
        #    vel[1] = randrange(0, 9)
        #else:
        #    vel[1] = randrange(-8, 0)

frame = simplegui.create_frame("Random ball with collision/reflection", width, height)
frame.set_draw_handler(draw)

frame.start()