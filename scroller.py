import time
import random
import os
os.system('')
red = "\033[101m  "
dark_red = "\033[41m"
orange = "\033[43m  "
yellow = "\033[103m  "
lime = "\033[102m  "
cyan = "\033[104m  "
blue = "\033[44m  "
purple = "\033[45m  "
black = "\033[40m  "
pink = "\033[105m  "
light_gray = "\033[47m  "
white = "\033[107m  "

color1 = white
color2 = light_gray

# Currently, this takes up way too much space. It's incredibly easy to optimize, but I don't feel like it right now.
while True:
    for i in range(9):
        print(color1 * 9 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 8 + color2 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 7 + color2 * 2 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 6 + color2 * 3 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 5 + color2 * 4 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 4 + color2 * 5 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 3 + color2 * 6 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 2 + color2 * 7 + black)
        time.sleep(.01)
    for i in range(9):
        print(color1 * 1 + color2 * 8 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 9 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 8 + color1 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 7 + color1 * 2 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 6 + color1 * 3 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 5 + color1 * 4 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 4 + color1 * 5 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 3 + color1 * 6 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 2 + color1 * 7 + black)
        time.sleep(.01)
    for i in range(9):
        print(color2 * 1 + color1 * 8 + black)
        time.sleep(.01)
