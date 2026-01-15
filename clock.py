import datetime
import time
import os
def bye():
    os.system("cls" if os.name == "nt" else "clear")
black = "\033[40m  "
white = "\033[107m  "
a = white + white + white + black # ⬜⬜⬜⬛
b = white + black + black + black # ⬜⬛⬛⬛
c = black + black + white + black # ⬛⬛⬜⬛
d = black + white + white + black # ⬛⬜⬜⬛
e = white + white + black + black # ⬜⬜⬛⬛
f = white + black # ⬜⬛
g = white + white + black + black # ⬜⬜⬛⬛
h = white + black + white + black # ⬜⬛⬜⬛
i = black + black # ⬛⬛
j = white + black + black + black + white + black # ⬜⬛⬛⬛⬜⬛
k = white + white + black + white + white + black # ⬜⬜⬛⬜⬜⬛
l = white + black + white + black + white + black # ⬜⬛⬜⬛⬜⬛
m = white + white + white + white + white + black # ⬜⬜⬜⬜⬜⬛
n = white + black + black + black + black + black # ⬜⬛⬛⬛⬛⬛
o = black + white + white + white + black + black # ⬛⬜⬜⬜⬜⬛
zerT = (a,h,h,h,a) # 0
oneT = (f,f,f,f,f) # 1
twoT = (a,c,a,b,a) # 2
thrT = (a,c,a,c,a) # 3
fouT = (h,h,a,c,c) # 4
fivT = (a,b,a,c,a) # 5
sixT = (a,b,a,h,a) # 6
sevT = (a,c,c,c,c) # 7
eigT = (a,h,a,h,a) # 8
ninT = (a,h,a,c,c) # 9
colT = (i,f,i,f,i) # 10
aaaT = (o,j,m,j,j) # 11
pppT = (m,j,m,n,n) # 12
mmmT = (j,k,l,j,j) # 13
fonT = (zerT,oneT,twoT,thrT,fouT,fivT,sixT,sevT,eigT,ninT,colT,aaaT,pppT,mmmT)
utc = int(input("Difference between your timezone and UTC?\nEST is -5, CST is -6, MST is -7, PST is -8.\nSometimes you have to enter 0 to get the correct time, too.\n"))
bye()
while True:
    date = datetime.datetime.now()
    hours = int(date.hour) + utc
    if hours < 0:
        hours = 0
    hour = (f"{hours:02d}")
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
    if hours > 12:
        for i in range(5):
            print(''.join((fonT[12])[i]) + ''.join((fonT[13])[i]))
    else:
        for i in range(5):
            print(''.join((fonT[11])[i]) + ''.join((fonT[13])[i]))
    print("\n")
    time.sleep(1)
    bye()