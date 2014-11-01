__author__ = 'clopez'

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

time = 0
mins = 0
secs = 0
decs = 0
strmin = "00"
strsec = "00"
strdsec = "000"
strout = strmin + ":" + strsec + ":" + strdsec


def format(t):
    global time, mins, secs, decs, strmin, strsec, strdsec, strout
  #  fsecs = time % 100
  #  fmins = secs % 60
  #  tstr = str(fmins) + ":" + str(fsecs)
  #  return tstr
    if time < 100:
        strdsec = "00" + str(time)
    elif 100 < time < 1000:
        strdsec = "0" + str(time)
    else:
        strdsec = str(time)
    secs = time % 100
    if secs < 10:
        strsec = "0" + str(secs)
    mins = secs % 60
    if mins < 10:
        strmin = "0" + str(mins)

    strout = strmin + ":" + strsec + "." + strdsec
    return strout


def start():
    timer.start()


def stop():
    timer.stop()


def reset():
    global time, strmin, strsec, strdsec, strout
    timer.stop()
    time = 0
    strmin = "00"
    strsec = "00"
    strdsec = "000"
    strout = strmin + ":" + strsec + "." + strdsec


def tick():
    global time
    time += 1
    print format(time)


def draw(canvas):
   # canvas.draw_text(strout, [20, 50], 48, "Orange", "sans-serif")
   canvas.draw_text(str(time), [20, 50], 48, "Orange", "sans-serif")

watchframe = simplegui.create_frame("Stopwatch", 300, 150)
watchframe.add_button("Start", start, 150)
watchframe.add_button("Stop", stop, 150)
watchframe.add_button("Reset", reset, 150)
watchframe.set_draw_handler(draw)
timer = simplegui.create_timer(10, tick)  # 1/10s
print watchframe.get_canvas_textwidth(strout, 48, "sans-serif")
watchframe.start()