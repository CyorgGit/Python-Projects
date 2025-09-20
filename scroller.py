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
# Change color1 and color2! A list of available colors is above.
color1 = white
color2 = light_gray
color3 = black
color1_amount = 9
color2_amount = 0
pattern = input("original, checkboard, or paul? ")
while True:
    if pattern == "original" or "":
        for i in range(9):
            for i in range(9):
                print(color1 * color1_amount + color2 * color2_amount + color3)
                time.sleep(.01)
            color1_amount = color1_amount - 1
            color2_amount = color2_amount + 1
        for i in range(9):
            for i in range(9):
                print(color2 * color2_amount + color1 * color1_amount + color3)
                time.sleep(.01)
            color1_amount = color1_amount + 1
            color2_amount = color2_amount - 1
    elif pattern == "checkerboard":
        print((color1 + color2) * 4 + color1 + color3)
        time.sleep(.01)
        print((color2 + color1) * 4 + color2 + color3)
        time.sleep(.01)
    elif pattern == "paul":
        random_number = random.randint(1,10)
        for i in range(random_number):
            random_number = random.randint(1,10)
            for i in range(random_number):
                print(str(" ") + color1 * color1_amount + color2 * color2_amount + color3)
                time.sleep(.01)
            random_number = random.randint(1,10)
            color1_amount = random_number
            random_number = random.randint(1,10)
            color2_amount = random_number
        random_number = random.randint(1,10)
        for i in range(random_number):
            random_number = random.randint(1,10)
            for i in range(random_number):
                print(color2 * color2_amount + color1 * color1_amount + color3)
                time.sleep(.01)
            random_number = random.randint(1,10)
            color1_amount = random_number
            random_number = random.randint(1,10)
            color2_amount = random_number
