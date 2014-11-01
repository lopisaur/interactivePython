__author__ = 'clopez'
# http://www.codeskulptor.org/#user38_GvuDuSIMos_9.py
# "Pong" - Assignment 4
# 20141018

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from random import randrange

# Initialize globals - pos and vel encode vertical info for paddles
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
ball_vel = []
# Velocity multiplier (10%)
ball_vel_multi = 1.1

# Paddle positions, initial vertical velocities, colors and scores
paddle1_pos = [HALF_PAD_WIDTH + 1, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle1_vel = 0
p1_col = "Orange"
score1 = 0

paddle2_pos = [WIDTH - HALF_PAD_WIDTH - 1, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle2_vel = 0
p2_col = "Indigo"
score2 = 0

quarterWidth = WIDTH / 4
textVPos = 75


# Initialize ball_pos and ball_vel for new ball in middle of table
# If direction is right, the ball's velocity is upper right, else upper LEFT
# So pass in the winning side, not the side where the ball hit...
# Assignment says randrange(120, 240) horizontal, (60, 180) vertical px/sec., that is (2, 4) / (1, 3) @60Hz.
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction:
        ball_vel = [randrange(2, 4), -randrange(1, 3)]
    else:
        ball_vel = [-randrange(2, 4), -randrange(1, 3)]


# Start new game
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2
    paddle1_pos = [HALF_PAD_WIDTH + 1, HEIGHT / 2 - HALF_PAD_HEIGHT]
    paddle1_vel = [0, 0]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH - 1, HEIGHT / 2 - HALF_PAD_HEIGHT]
    paddle2_vel = [0, 0]
    score1 = 0
    score2 = 0
    # Booleans are integers in Python, so this works.
    spawn_ball(randrange(0, 2))


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # Draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # Render scores earlier than the template so the ball is "above" the text.
    canvas.draw_text(str(score1), [quarterWidth, textVPos], 36, p1_col, "sans-serif")
    canvas.draw_text(str(score2), [3 * quarterWidth, textVPos], 36, p2_col, "sans-serif")
    # Update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Horizontal collision: Left paddle, right paddle, left gutter, right gutter.
    # Reverse horizontal direction and increase overall velocity after hitting a paddle.
    # When the ball hits the gutter, call spawn_ball with the side that has won.
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and (paddle1_pos[1] + PAD_HEIGHT >= ball_pos[1] >= paddle1_pos[1]):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= ball_vel_multi
        ball_vel[1] *= ball_vel_multi
    elif ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS) and (paddle2_pos[1] + PAD_HEIGHT
                                                               >= ball_pos[1] >= paddle2_pos[1]):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= ball_vel_multi
        ball_vel[1] *= ball_vel_multi
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS):
        score1 += 1
        spawn_ball(LEFT)

    # Vertical collision
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
        ball_vel[1] = -ball_vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # Update paddle's vertical position, keep paddle on the screen
    # See comment for keydown()
    paddle1_pos[1] += paddle1_vel[1]
    if paddle1_pos[1] == 0 or paddle1_pos[1] > HEIGHT - PAD_HEIGHT - 1:
        paddle1_vel[1] = 0
    paddle2_pos[1] += paddle2_vel[1]
    if paddle2_pos[1] == 0 or paddle2_pos[1] > HEIGHT - PAD_HEIGHT - 1:
        paddle2_vel[1] = 0

    # Draw Paddles
    canvas.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, p1_col)
    canvas.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, p2_col)


# We need to check positions here too.
# If we don't, the paddle will go off screen if we press the same key again after it has hit the floor or ceiling.
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] and paddle1_pos[1] > 0:
        paddle1_vel[1] -= 5
    if key == simplegui.KEY_MAP["s"] and paddle1_pos[1] < HEIGHT - PAD_HEIGHT - 1:
        paddle1_vel[1] += 5
    if key == simplegui.KEY_MAP["up"] and paddle2_pos[1] > 0:
        paddle2_vel[1] -= 5
    if key == simplegui.KEY_MAP["down"] and paddle2_pos[1] < HEIGHT - PAD_HEIGHT - 1:
        paddle2_vel[1] += 5

# Stop moving when key is released
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0


# Create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restartButton = frame.add_button("Restart", new_game, 150)
# Start frame
new_game()
frame.start()
