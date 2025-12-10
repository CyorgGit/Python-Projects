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
print(color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color3 + color3 + color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + "\n" + color1 + color3 + color3 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color1 + color3 + "\n" + color1 + color1 + color1 + color3 + color1 + color3 + color3 + color3 + color1 + color1 + color3 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color3 + color3 + color1 + color1 + color3 + color3 + color1 + color1 + color3 + color3 + "\n" + color3 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color3 + color3 + color1 + color3 + color1 + color3 + "\n" + color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color3 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color1 + color1 + color3 + color1 + color3 + color1 + color3)
pattern = input("\n\033[4mChoose one!\n\n\033[0mOriginal - Spinning thing.\nCheckerboard - Checkerboard/Chess pattern.\nCheckerboard 2.0 - Spinning checkerboard!\nPaul\nWater - Waterfall.\nRainbow - Wavy rainbow.\nVertical - Stairs, or an infinitely rotating cube.\nZig-Zag Text - Text goes from side to side.\nPortal - Original, but now with portals added!\nPortal Text - Zig-zag text, but with portals.\nStatic - Glitchy.\nMatrix - Green falling text.\n\n\033[32m> \033[4m")
print("\033[0m")
while True:
        if pattern.lower() == "original" or "":
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
        elif pattern.lower() == "checkerboard":
            print((color1 + color2) * 4 + color1 + color3)
            time.sleep(.01)
            print((color2 + color1) * 4 + color2 + color3)
            time.sleep(.01)
        elif pattern.lower() == "paul":
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
        elif pattern.lower() == "water":
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
        elif pattern.lower() == "rainbow":
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
        elif pattern.lower() == "vertical":
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
        elif pattern.lower() == "text":
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
        elif pattern.lower() == "zig-zag text":
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
        elif pattern.lower() == "portal":
            print(cyan * 13 + black)
            print(cyan + white * 11 + cyan + black)
            print(cyan * 2 + white * 9 + cyan * 2 + black)
            for i in range(9):
                for i in range(9):
                    print("    " + color1 * color1_amount + color2 * color2_amount + color3)
                    time.sleep(.01)
                color1_amount = color1_amount - 1
                color2_amount = color2_amount + 1
            for i in range(9):
                for i in range(9):
                    print("    " + color2 * color2_amount + color1 * color1_amount + color3)
                    time.sleep(.01)
                color1_amount = color1_amount + 1
                color2_amount = color2_amount - 1
            print(orange * 2 + white * 9 + orange * 2 + black)
            print(orange + white * 11 + orange + black)
            print(orange * 13 + black)
            for i in range(50):
                print("\n")
                time.sleep(.01)
        elif pattern.lower() == "portal text":
            s = input("Type something! ")
            while True:
                print(cyan * (len(s) + 1) + black)
                time.sleep(.01)
                print(cyan + white * (len(s) - 1) + cyan + black)
                time.sleep(.01)
                print(cyan * 2 + white * (len(s) - 3) + cyan * 2 + black)
                time.sleep(.01)
                s1 = 0
                for i in range(len(s)):
                    print("    " + color3 * color3_amount + s[s1:] + color3)
                    s1 = s1 + 1
                    color3_amount = color3_amount + 1
                    time.sleep(0.01)
                s1 = len(s) - 1
                for i in range(len(s)):
                    print("    " + color3 * color3_amount + s[s1:] + color3)
                    s1 = s1 - 1
                    color3_amount = color3_amount - 1
                    time.sleep(0.01)
                s1 = 0
                print(orange * 2 + white * (len(s) - 3) + orange * 2 + black)
                time.sleep(.01)
                print(orange + white * (len(s) - 1) + orange + black)
                time.sleep(.01)
                print(orange * (len(s) + 1) + black)
                time.sleep(.01)
                for i in range(50):
                    print("\n")
                    time.sleep(.01)
        elif pattern.lower() == "checkerboard 2.0":
            for i in range(9):
                for i in range(9):
                    print((color2 + color1) * color1_amount + color3)
                    time.sleep(.01)
                    print((color1 + color2) * color1_amount + color3)
                    time.sleep(.01)
                color1_amount = color1_amount - 1
                color2_amount = color2_amount + 1
            for i in range(9):
                for i in range(9):
                    print((color2 + color1) * color1_amount + color3)
                    time.sleep(.01)
                    print((color1 + color2) * color1_amount + color3)
                    time.sleep(.01)
                color1_amount = color1_amount + 1
                color2_amount = color2_amount - 1
        elif pattern.lower() == "static":
            print("Epilepsy warning!\nTry changing the size of the window!\nResults heavily depend on the width of the terminal.")
            time.sleep(2)
            while True:
                for i in range(9):
                    print((color3 * 3 + color1 * 3) * color1_amount + color3)
                    time.sleep(.01)
                    color1_amount - 1
                for i in range(9):
                    print((color3 * 3 + color1 * 3) * color1_amount + color3)
                    time.sleep(.01)
                    color1_amount = color1_amount + 1
        elif pattern.lower() == "one":
            print(black * 4 + white + black + "\n" + black * 3 + white * 2 + black + "\n" + (black * 4 + white + black + "\n") * 2 + black * 3 + white * 3 + black)
            time.sleep(1)
            break
        elif pattern.lower() == "matrix":
            def matrix():
                sm = str("")
                for i in range(10):
                    rm = random.randint(0,(len(s) - 1))
                    srm = random.randint(0,3)
                    sm = sm + (" "*srm) + mList[rm]
                print(sm)
            s = input("Type something! \033[92m")
            print(black)
            mList = list(s)
            while True:
                sm = str("")
                for i in range(10):
                    matrix()
                    time.sleep(.01)
        else:
            print("Choose something that actually works!")
            time.sleep(1)
            break
