__author__ = 'clopez'
# ballDrop
# 20141014

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width = 600
height = 400
radius = 20

pos = [width / 2, height / 2]
vel = [1, 3]
direction = ["", ""]



def draw(canvas):
    global direction1
    pos[0] += vel[0]
    pos[1] += vel[1]
    canvas.draw_circle(pos, radius, 2, "White", "Blue")
    if pos[0] < radius or pos[0] > width - radius:
        vel[0] = -vel[0]
    if pos[1] < radius or pos[1] > height - radius:
        vel[1] = -vel[1]
    if vel[0] < 0:
        direction[0] = "left"
    if vel[0] > 0:
        direction[0] = "right"
    if vel[1] < 0:
        direction[1] = "up"
    if vel[1] > 0:
        direction[1] = "down"


def keydown(key):
    if key == simplegui.KEY_MAP["left"]:
        vel[0] = -vel[0]
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] = -vel[0]
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] -vel[1]
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] -vel[1]
    print direction

frame = simplegui.create_frame("Ball drop without timer", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.start()