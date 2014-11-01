__author__ = 'clopez'

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

time = 0
attempts = 0
hits = 0

# This one works
# def format(t):
#     dsecs = t % 10
#     secs = (t // 10) % 60
#     mins = t // 600
#     if mins < 10:
#         minutes = "0" + str(mins)
#     else:
#         minutes = str(mins)
#     if secs < 10:
#         seconds = "0" + str(secs)
#     else:
#         seconds = str(secs)
#     strout = minutes + ":" + seconds + "." + str(dsecs)
#     return strout

def format(t):
    seconds = str((t // 10) % 60)
    if ((t // 10) % 60) < 10:
        seconds = "0" + seconds
    return str(t // 600) + ":" + seconds + "." + str(t % 10)

def start():
    timer.start()


def stop():
    global attempts, hits
    if timer.is_running():
        timer.stop()
        attempts += 1
        if time % 10 == 0:
            hits += 1
        print "attempts: " + str(attempts), "hits: " + str(hits)


def reset():
    global time, attempts, hits
    timer.stop()
    time = 0
    attempts = 0
    hits = 0


def tick():
    global time
    time += 1
    print time


def draw(canvas):
    canvas.draw_text(format(time), [20, 80], 48, "Orange", "sans-serif")
    if attempts > 0:
        canvas.draw_text(str(hits) + "/" + str(attempts), [250, 20], 18, "Red", "sans-serif")


watchframe = simplegui.create_frame("Stopwatch", 300, 150)
watchframe.add_button("Start", start, 150)
watchframe.add_button("Stop", stop, 150)
watchframe.add_button("Reset", reset, 150)
watchframe.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)  # 1/10s
#timer = simplegui.create_timer(1, tick)  # Test
watchframe.start()