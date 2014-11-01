__author__ = 'clopez'

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

time = 0
mins = 0
attempts = 0
hits = 0
#secs = 0
strout = "00:00.0"


def format(t):
    global time, mins, strout
    secs = float(t)/10
    if secs == 60:
        secs = 0
        time = 0
        mins += 1
    if mins < 10:
        strmin = "0" + str(mins)
    else:
        strmin = str(mins)
    if secs == 0:
        strsec = "00.0"
    elif secs < 10:
        strsec = "0" + str(secs)
    else:
        strsec = str(secs)
    strout = strmin + ":" + strsec
    return strout


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
    global time, mins, strout, attempts, hits
    timer.stop()
    time = 0
    mins = 0
    attempts = 0
    hits = 0
    strout = "00:00.0"


def tick():
    global time
    time += 1
    print time
    format(time)


def draw(canvas):
    canvas.draw_text(strout, [20, 80], 48, "Orange", "sans-serif")
    if attempts > 0:
        canvas.draw_text(str(hits) + "/" + str(attempts), [250, 20], 18, "Red", "sans-serif")
    # canvas.draw_text(str(time), [20, 50], 48, "Orange", "sans-serif")

watchframe = simplegui.create_frame("Stopwatch", 300, 150)
watchframe.add_button("Start", start, 150)
watchframe.add_button("Stop", stop, 150)
watchframe.add_button("Reset", reset, 150)
watchframe.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)  # 1/10s
#timer = simplegui.create_timer(1, tick)  # Test
watchframe.start()