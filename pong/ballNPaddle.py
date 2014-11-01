__author__ = 'clopez'
# ballNPaddle - Combine paddle.py and randomBallReflection.py
# 20141016

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange

width = 600
height = 400
paddle_width, paddle_height = 20, 100
radius = 20

ball_pos = [width / 2, height / 2]
#vel = [1, 3]
vel = [randrange(-8, 9), randrange(-8, 9)]

left_pos = [10, 10]
left_vel = [0, 3]
#left_vel = [0, randrange(1, 11)]
left_direction = "down"

right_pos = [(width - paddle_width - 1), 10]
right_vel = [0, 3]
#right_vel = [0, randrange(1, 11)]
right_direction = "down"


def draw(canvas):
    global left_direction, right_direction
    # Left paddle
    if left_vel[1] < 0:
        left_direction = "up"
    else:
        left_direction = "down"
    left_pos[1] += left_vel[1]
    canvas.draw_line(left_pos, [left_pos[0], left_pos[1] + paddle_height], paddle_width, "Blue")
    if left_pos[1] <= 0 or left_pos[1] >= height - paddle_height - 1:
        left_vel[1] = - left_vel[1]
        print ("Left paddle vertical collision")

    # Right paddle
    if right_vel[1] < 0:
        right_direction = "up"
    else:
        right_direction = "down"
    right_pos[1] += right_vel[1]
    canvas.draw_line(right_pos, [right_pos[0], right_pos[1] + paddle_height], paddle_width, "Yellow")
    if right_pos[1] <= 0 or right_pos[1] >= height - paddle_height - 1:
        right_vel[1] = - right_vel[1]
        print ("Right paddle vertical collision")


frame = simplegui.create_frame("ballNPaddle", width, height)
frame.set_draw_handler(draw)

frame.start()