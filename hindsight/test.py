#!/usr/bin/env python3
import subprocess
import sys

# https://askubuntu.com/questions/702071/move-windows-to-specific-screens-using-the-command-line

# just a helper function, to reduce the amount of code
get = lambda cmd: subprocess.check_output(cmd).decode("utf-8")

# get the data on all currently connected screens, their x-resolution
screendata = [l.split() for l in get(["xrandr"]).splitlines() if " connected" in l]
screendata = sum([[(w[0], s.split("+")[-2]) for s in w if s.count("+") == 2] for w in screendata], [])

print(screendata)

# def get_class(classname):
#     # function to get all windows that belong to a specific window class (application)
#     w_list = [l.split()[0] for l in get(["wmctrl", "-l"]).splitlines()]
#     return [w for w in w_list if classname in get(["xprop", "-id", w])]

# scr = sys.argv[2]

# try:
#     # determine the left position of the targeted screen (x)
#     pos = [sc for sc in screendata if sc[0] == scr][0]
# except IndexError:
#     # warning if the screen's name is incorrect (does not exist)
#     print(scr, "does not exist. Check the screen name")
# else:
#     for w in get_class(sys.argv[1]):
#         # first move and resize the window, to make sure it fits completely inside the targeted screen
#         # else the next command will fail...
#         subprocess.Popen(["wmctrl", "-ir", w, "-e", "0,"+str(int(pos[1])+100)+",100,300,300"])
#         # maximize the window on its new screen
#         subprocess.Popen(["xdotool", "windowsize", "-sync", w, "100%", "100%"])
