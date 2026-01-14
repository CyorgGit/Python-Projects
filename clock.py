import datetime
import time
import os
def bye():
    os.system("cls" if os.name == "nt" else "clear")
black = "\033[40m  "
white = "\033[107m  "
color = white
a = color + color + color + black # ⬜⬜⬜⬛
b = color + black + black + black # ⬜⬛⬛⬛
c = black + black + color + black # ⬛⬛⬜⬛
d = black + color + color + black # ⬛⬜⬜⬛
e = color + color + black + black # ⬜⬜⬛⬛
f = color + black # ⬜⬛
g = color + color + black + black # ⬜⬜⬛⬛
h = color + black + color + black # ⬜⬛⬜⬛
i = black + black # ⬛⬛
zerT = (a,h,h,h,a)
oneT = (f,f,f,f,f)
twoT = (a,c,a,b,a)
thrT = (a,c,a,c,a)
fouT = (h,h,a,c,c)
fivT = (a,b,a,c,a)
sixT = (a,b,a,h,a)
sevT = (a,c,c,c,c)
eigT = (a,h,a,h,a)
ninT = (a,h,a,c,c)
colT = (i,f,i,f,i)
fonT = (zerT,oneT,twoT,thrT,fouT,fivT,sixT,sevT,eigT,ninT,colT)
utc = int(input("Difference between your timezone and UTC?\nEST is -5, CST is -6, MST is -7, PST is -8.\nSometimes you have to enter 0 to get the correct time, too.\n"))
bye()
while True:
    date = datetime.datetime.now()
    hour = (int((f"{date.hour:02d}")) + utc)
    hour_one = int(str(hour)[:1])
    hour_two = int(str(hour)[1:])
    minute = (f"{date.minute:02d}")
    minute_one = int(str(minute)[:1])
    minute_two = int(str(minute)[1:])
    second = (f"{date.second:02d}")
    second_one = int(str(second)[:1])
    second_two = int(str(second)[1:])
    colon = 10
    for i in range(5):
        print(''.join((fonT[hour_one])[i]) + ''.join((fonT[hour_two])[i]) + ''.join((fonT[colon])[i]) + ''.join((fonT[minute_one])[i]) + ''.join((fonT[minute_two])[i]) + ''.join((fonT[colon])[i]) + ''.join((fonT[second_one])[i]) + ''.join((fonT[second_two])[i]))
    print("\n")
    time.sleep(1)
    bye()
