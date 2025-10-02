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
rainbow = red + orange + yellow + lime + cyan + blue + purple + black
# Change color1 and color2! A list of available colors is above.
color1 = white
color2 = light_gray
color3 = black
color1_amount = 9
color2_amount = 0
color3_amount = 0
pattern = input("original, checkboard, paul, water, rainbow, vertical, text, or zig-zag text? ")
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
    elif pattern == "water":
        for i in range(9):
            random_number = random.randint(1,10)
            for i in range(random_number):
                print(str(" ") + blue * color1_amount + cyan * color2_amount + blue * color1_amount + blue)
                time.sleep(.01)
            random_number = random.randint(1,10)
            color1_amount = random_number
            random_number = random.randint(1,5)
            color2_amount = random_number
        random_number = random.randint(1,10)
        random_number = random.randint(1,10)
        for i in range(9):
            random_number = random.randint(1,10)
            for i in range(random_number):
                print(str(" ") + cyan * color2_amount + blue * color1_amount + cyan * color1_amount + blue)
                time.sleep(.01)
            random_number = random.randint(1,7)
            color1_amount = random_number
            random_number = random.randint(1,5)
            color2_amount = random_number
    elif pattern == "rainbow":
        print(rainbow)
        time.sleep(.01)
        print(str(" ") + rainbow)
        time.sleep(.01)
        print(str("  ") + rainbow)
        time.sleep(.01)
        print(str("   ") + rainbow)
        time.sleep(.01)
        print(str("  ") + rainbow)
        time.sleep(.01)
        print(str(" ") + rainbow)
        time.sleep(.01)
    elif pattern == "vertical":
        color1_amount = 25
        for i in range(5):
            for i in range(5):
                print(color3 * color3_amount + color1 * color1_amount + color3 * color3_amount + color3)
                time.sleep(.01)
            color1_amount = color1_amount - 2
            color2_amount = color2_amount + 1
            color3_amount = color3_amount + 1
        color1_amount = 15
        for i in range(5):
            for i in range(5):
                print(color3 * color3_amount + color2 * color1_amount + color3 * color3_amount)
                time.sleep(.01)
            color1_amount = color1_amount + 2
            color2_amount = color2_amount - 1
            color3_amount = color3_amount - 1
    elif pattern == "text":
        s = input("Type something! ")
        s1 = 0
        while True:
            for i in range(len(s)):
                print(s[s1:])
                s1 = s1 + 1
                time.sleep(0.01)
            s1 = len(s) - 1
            for i in range(len(s)):
                print(s[s1:])
                s1 = s1 - 1
                time.sleep(0.01)
            s1 = 0
    elif pattern == "zig-zag text":
        s = input("Type something! ")
        s1 = 0
        while True:
            for i in range(len(s)):
                print(color3 * color3_amount + s[s1:] + color3)
                s1 = s1 + 1
                color3_amount = color3_amount + 1
                time.sleep(0.01)
            s1 = len(s) - 1
            for i in range(len(s)):
                print(color3 * color3_amount + s[s1:] + color3)
                s1 = s1 - 1
                color3_amount = color3_amount - 1
                time.sleep(0.01)
            s1 = 0
    else:
        print("Choose something that actually works!")
        time.sleep(1)
        break
