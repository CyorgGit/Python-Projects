import random
red = "\033[101m  "
orange = "\033[43m  "
green = "\033[42m  "
black = "\033[40m  "
white = "\033[107m  "
random_num = random.randint(0,100)
if random_num != 85:
    color1 = red
    color2 = orange
    color3 = green
else:
    color1 = white
    color2 = orange
    color3 = green
a = black * 3 + color1 * 5 + black * 5
b = black * 2 + color1 * 9 + black * 2
c = black * 2 + color3 * 3 + color2 * 2 + color3 + color2 + black * 4
d = black + color3 + color2 + color3 + color2 * 3 + color3 + color2 * 3 + black * 2
e = black + color3 + color2 + color3 * 2 + color2 * 3 + color3 + color2 * 3 + black
f = black + color3 * 2 + color2 * 4 + color3 * 4 + black
g = black * 3 + color2 * 7 + black * 3
h = black * 2 + color3 * 2 + color1 + color3 * 3 + black * 5
i = black + color3 * 3 + color1 + color3 * 2 + color1 + color3 * 3 + black * 2
j = color3 * 4 + color1 * 4 + color3 * 4 + black
k = color2 * 2 + color3 + color1 + color2 + color1 * 2 + color2 + color1 + color3 + color2 * 2 + black
l = color2 * 3 + color1 * 6 + color2 * 3 + black
m = color2 * 2 + color1 * 8 + color2 * 2 + black
n = black * 2 + color1 * 3 + black * 2 + color1 * 3 + black * 3
o = black + color3 * 3 + black * 4 + color3 * 3 + black * 2
p = color3 * 4 + black * 4 + color3 * 4 + black
z = "\n"
print(a + z + b + z + c + z + d + z + e + z + f + z + g + z + h + z + i + z + j + z + k + z + l + z + m + z + n + z + o + z + p)
