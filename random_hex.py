import random
import os
os.system("")
red = "\033[101m  "
lime = "\033[102m  "
blue = "\033[44m  "
code = ""
valid_values = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")
for i in range(6):
    thing = random.randint(0,15)
    character = valid_values[thing]
    code = code + character
print(code)
no1 = 0
rgb_values = []
rgb_percent = []
rgb_firstdigit = []
for i in range(3):
    hexcode = code[(no1):(no1+2)]
    deccode = int(hexcode, 16)
    rgb_values.append(deccode)
    no1 = no1 + 2
total_rgb = rgb_values[0] + rgb_values[1] + rgb_values[2]
no1 = 0
for i in range(3):
    rgb_divide = rgb_values[no1] / total_rgb
    rgb_round = ((round((rgb_divide * 100))))
    rgb_double = f'{rgb_round:02d}'
    rgb_percent.append(rgb_double)
    rgb_thing = round((int(rgb_percent[no1]) / 10))
    rgb_firstdigit.append(rgb_thing)
    no1 = no1 + 1
print("\n" + str(rgb_percent[0]) + "% red, " + str(rgb_percent[1]) + "% green, " + str(rgb_percent[2]) + "% blue")
print(red*rgb_firstdigit[0] + lime*rgb_firstdigit[1] + blue*rgb_firstdigit[2] + "\033[0m")
input()