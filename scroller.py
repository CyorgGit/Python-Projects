import time
import random
import os
os.system('')
red = "\033[101m  "
dark_red = "\033[41m  "
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
color1_amount = 9
color2_amount = 0
    
while True:
    for i in range(9):
        for i in range(9):
            print(color1 * color1_amount + color2 * color2_amount + black)
            time.sleep(.01)
        color1_amount = color1_amount - 1
        color2_amount = color2_amount + 1
    for i in range(9):
        for i in range(9):
            print(color2 * color2_amount + color1 * color1_amount + black)
            time.sleep(.01)
        color1_amount = color1_amount + 1
        color2_amount = color2_amount - 1
