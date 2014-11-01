__author__ = 'clopez'
# ballPos
# 20141014

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width = 600
height = 400
radius = 20

ball_pos = [width / 2, height / 2]


def draw(canvas):
    global ball_pos
    canvas.draw_circle(ball_pos, radius, 2, "White", "Blue")
    if ball_pos[0] < radius or ball_pos[0] > width - radius:
        print "horizontal collision"
        ball_pos = [width / 2, height / 2]
    if ball_pos[1] < radius or ball_pos[1] > height - radius:
        print "vertical collision"
        ball_pos = [width / 2, height / 2]


def keydown(key):
    vel = 4
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= vel
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += vel
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += vel
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= vel


frame = simplegui.create_frame("Ball control", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

frame.start()