__author__ = 'clopez'
# http://www.codeskulptor.org/#user38_DGbj2QfRyS_1.py
# "Stopwatch" - Assignment 3
# 20141011

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Running time, attempts and correct clicks.
time = 0
attempts = 0
hits = 0


# We only need to worry about formatting the seconds.
# Put the value in a local variable so we don't have to calculate it twice.
def format(t):
    secs = (t // 10) % 60
    seconds = str(secs)
    if secs < 10:
        seconds = "0" + seconds
    return str(t // 600) + ":" + seconds + "." + str(t % 10)


def start():
    timer.start()


# Do nothing if the timer is not running.
# If it is, stop it, increase number of attempts and hits if the click was on a whole second.
def stop():
    global attempts, hits
    if timer.is_running():
        timer.stop()
        attempts += 1
        if time % 10 == 0:
            hits += 1


# Stop timer, reset all global variables.
def reset():
    global time, attempts, hits
    timer.stop()
    time = 0
    attempts = 0
    hits = 0


def tick():
    global time
    time += 1

# Only show the number of attempts and hits if "Stop" was pressed at least once.
def draw(canvas):
    canvas.draw_text(format(time), [40, 75], 48, "Orange", "sans-serif")
    if attempts > 0:
        canvas.draw_text(str(hits) + "/" + str(attempts), [190, 20], 16, "Red", "sans-serif")

# We need some space to the right in case we reach 10 minutes...
watchframe = simplegui.create_frame("Stopwatch", 240, 120)
watchframe.add_button("Start", start, 150)
watchframe.add_button("Stop", stop, 150)
watchframe.add_button("Reset", reset, 150)
watchframe.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

watchframe.start()