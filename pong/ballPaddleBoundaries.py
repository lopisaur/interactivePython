__author__ = 'clopez'
# http://www.codeskulptor.org/
# "xxx" - Assignment 3
# 20141018

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
# If we hit a paddle, increase velocity by 10%
ball_vel_multi = 1.1

paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle1_vel = 0

paddle1UpperBound = paddle1_pos[1]
paddle1LowerBound = paddle1UpperBound + PAD_HEIGHT

paddle2_pos = [WIDTH - HALF_PAD_WIDTH - 1, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle2_vel = 0

score1 = 0
score2 = 0

left_gutter = BALL_RADIUS
right_gutter = WIDTH - BALL_RADIUS - 1
ballUpperBound = ball_pos[1] - BALL_RADIUS
ballLowerBound = ball_pos[1] + BALL_RADIUS
laserColor = "Blue"


def draw(canvas):
    canvas.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, "Orange")
    canvas.draw_line([0, paddle1UpperBound], [WIDTH, paddle1UpperBound], 1, "White")
    canvas.draw_line([0, paddle1LowerBound], [WIDTH, paddle1LowerBound], 1, "White")
    canvas.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, "Orange")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "Orange")
    canvas.draw_line([0, ballUpperBound], [ball_pos[0], ballUpperBound], 1, laserColor)
    canvas.draw_line([0, ballLowerBound], [ball_pos[0], ballLowerBound], 1, laserColor)


def keydown(key):
    global ball_pos, ballUpperBound, ballLowerBound, laserColor
    if key == simplegui.KEY_MAP["u"]:
        ball_pos[1] -= ball_vel[1]
    if key == simplegui.KEY_MAP["j"]:
        ball_pos[1] += ball_vel[1]
    if key == simplegui.KEY_MAP["h"]:
        ball_pos[0] -= ball_vel[0]
    if key == simplegui.KEY_MAP["k"]:
        ball_pos[0] += ball_vel[0]
    ballUpperBound = ball_pos[1] - BALL_RADIUS
    ballLowerBound = ball_pos[1] + BALL_RADIUS
    if ballUpperBound < paddle1UpperBound or ballLowerBound > paddle1LowerBound:
        laserColor = "Red"
    else:
        laserColor = "Blue"
    print("ball_pos (center):", ball_pos)
    print("ball upper bound:", ballUpperBound)
    print("ball lower bound:", ballLowerBound)


def keyup(key):
    if key == simplegui.KEY_MAP["u"] or key == simplegui.KEY_MAP["j"]:
        ball_vel[1] = 0
    if key == simplegui.KEY_MAP["h"] or key == simplegui.KEY_MAP["k"]:
        ball_vel[0] = 0

print("ball_pos (center):", ball_pos)
print("ball upper bound:", ballUpperBound)
print("ball lower bound:", ballLowerBound)
frame = simplegui.create_frame("ballPaddleBoundaries", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()
