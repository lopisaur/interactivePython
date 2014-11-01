__author__ = 'clopez'
# paddle control
# 20141014

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width = 600
height = 400
paddle_width, paddle_height = 20, 100

pos = [10, 10]
vel = [0, 3]
direction = "down"


def draw(canvas):
    global direction
    if vel[1] < 0:
        direction = "up"
    else:
        direction = "down"
    pos[1] += vel[1]
    canvas.draw_line(pos, [pos[0], pos[1] + paddle_height], paddle_width, "Blue")
    if pos[1] <= 0 or pos[1] >= height - paddle_height:
        vel[1] = - vel[1]
        print "wall collision"


def pcontrol(key):
    if key == simplegui.KEY_MAP["up"] and direction == "down":
        vel[1] = - vel[1]
    if key == simplegui.KEY_MAP["down"] and direction == "up":
        vel[1] = abs(vel[1])
    print direction


frame = simplegui.create_frame("Paddle control", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(pcontrol)

frame.start()

#
#
#def keydown(key):
#    if key == simplegui.KEY_MAP["left"]:
#        vel[0] = -vel[0]
#    elif key == simplegui.KEY_MAP["right"]:
#        vel[0] = -vel[0]
#    elif key == simplegui.KEY_MAP["down"]:
#        vel[1] -vel[1]
#    elif key == simplegui.KEY_MAP["up"]:
#        vel[1] -vel[1]
#    print direction
#
#frame = simplegui.create_frame("Ball drop without timer", width, height)
#frame.set_draw_handler(draw)
#frame.set_keydown_handler(keydown)
#frame.start()
#
#
#
#width = 600
#height = 400
#paddle_width, paddle_height = 20, 100
#start_pos = [10, 10]
#vel = [0, 10]
#time = 0
#
#
#def tick():
#    global time
#    time += 1
#
#
#def draw(canvas):
#    curr_pos = [0, 0]
#    curr_pos[0] = start_pos[0] + time * vel[0]
#    curr_pos[1] = start_pos[1] + time * vel[1]
#    canvas.draw_line(curr_pos, [curr_pos[0], curr_pos[1] + paddle_height], paddle_width, "Blue")
#    print time, curr_pos
#
#
#frame = simplegui.create_frame("Paddle control", width, height)
#frame.set_draw_handler(draw)
#timer = simplegui.create_timer(100, tick)
#
#frame.start()
#timer.start()