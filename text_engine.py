import os
os.system("")
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
o = black + white + black + black + white + black # ⬛⬜⬛⬛⬜⬛
p = white + white + white + white + black + black # ⬜⬜⬜⬜⬛⬛
q = white + black + white + white + white + black # ⬜⬛⬜⬜⬜⬛
r = black + black + white + black + black + black # ⬛⬛⬜⬛⬛⬛
s = white + white + white + black + black + black # ⬜⬜⬜⬛⬛⬛
t = black + black + black + white + black + black # ⬛⬛⬛⬜⬛⬛
u = white + black + white + black + black + black # ⬜⬛⬜⬛⬛⬛
v = white + black + black + white + black + black # ⬜⬛⬛⬜⬛⬛
w = white + white + black + black + white + black # ⬜⬜⬛⬛⬜⬛
x = white + black + black + white + white + black # ⬜⬛⬛⬜⬜⬛
y = white + white + white + black + white + black # ⬜⬜⬜⬛⬜⬛
z = black + black + black + black + white + black # ⬛⬛⬛⬛⬜⬛
A = black + white + black + white + black + black # ⬛⬜⬛⬜⬛⬛
B = black + white + black + black # ⬛⬜⬛⬛
C = black + black + black + black # ⬛⬛⬛⬛
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
aaaT = (m,j,m,j,j) # 11
bbbT = (m,j,p,j,m) # 12
cccT = (m,n,n,n,m) # 13
dddT = (p,j,j,j,p) # 14
eeeT = (m,n,p,n,m) # 15
fffT = (m,n,p,n,n) # 16
gggT = (m,n,q,j,m) # 17
hhhT = (j,j,m,j,j) # 18
iiiT = (m,r,r,r,m) # 19
jjjT = (m,r,r,u,s) # 20
kkkT = (j,v,s,v,j) # 21
lllT = (n,n,n,n,m) # 22
mmmT = (j,k,l,j,j) # 23
nnnT = (j,w,l,x,j) # 24
oooT = (m,j,j,j,m) # 25
pppT = (m,j,m,n,n) # 26
qqqT = (m,j,j,v,y) # 27
rrrT = (m,j,m,v,j) # 28
sssT = (m,n,m,z,m) # 29
tttT = (m,r,r,r,r) # 30
uuuT = (j,j,j,j,m) # 31
vvvT = (j,j,j,A,r) # 32
wwwT = (j,j,j,l,k) # 33
xxxT = (j,A,r,A,j) # 34
yyyT = (j,A,r,r,r) # 35
zzzT = (m,v,r,o,m) # 36
excT = (f,f,f,i,f) # 37
colT = (i,f,i,f,i) # 38
apoT = (f,f,i,i,i) # 39
lpaT = (d,b,b,b,d) # 40
rpaT = (e,c,c,c,e) # 41
astT = (h,B,h,C,C) # 42
pluT = (C,B,a,B,C) # 43
comT = (i,i,i,f,f) # 44
equT = (C,a,C,a,C) # 45
perT = (i,i,i,i,f) # 46
spaT = (C,C,C,C,C) # 47
queT = (a,c,d,C,B) # 48
lbrT = (a,b,b,b,a) # 49
rbrT = (a,c,c,c,a) # 50
lesT = (c,B,b,B,c) # 51
greT = (b,B,c,B,b) # 52
fonT = (zerT,oneT,twoT,thrT,fouT,fivT,sixT,sevT,eigT,ninT,colT,aaaT,bbbT,cccT,dddT,eeeT,fffT,gggT,hhhT,iiiT,jjjT,kkkT,lllT,mmmT,nnnT,oooT,pppT,qqqT,rrrT,sssT,tttT,uuuT,vvvT,wwwT,xxxT,yyyT,zzzT,excT,colT,apoT,lpaT,rpaT,astT,pluT,comT,equT,perT,spaT,queT,lbrT,rbrT,lesT,greT)
for i in range(5):
    print("".join((fonT[11])[i]) + "".join((fonT[12])[i]) + "".join((fonT[13])[i]) + "".join((fonT[14])[i]) + "".join((fonT[15])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[16])[i]) + "".join((fonT[17])[i]) + "".join((fonT[18])[i]) + "".join((fonT[19])[i]) + "".join((fonT[20])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[21])[i]) + "".join((fonT[22])[i]) + "".join((fonT[23])[i]) + "".join((fonT[24])[i]) + "".join((fonT[25])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[26])[i]) + "".join((fonT[27])[i]) + "".join((fonT[28])[i]) + "".join((fonT[29])[i]) + "".join((fonT[30])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[31])[i]) + "".join((fonT[32])[i]) + "".join((fonT[33])[i]) + "".join((fonT[34])[i]) + "".join((fonT[35])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[36])[i]) + "".join((fonT[0])[i]) + "".join((fonT[1])[i]) + "".join((fonT[2])[i]) + "".join((fonT[3])[i]) + "".join((fonT[4])[i]) + "".join((fonT[5])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[6])[i]) + "".join((fonT[7])[i]) + "".join((fonT[8])[i]) + "".join((fonT[9])[i]) + "".join((fonT[37])[i]) + "".join((fonT[38])[i]) + "".join((fonT[39])[i]) + "".join((fonT[43])[i]) + "".join((fonT[45])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[46])[i]) + "".join((fonT[44])[i]) + "".join((fonT[40])[i]) + "".join((fonT[41])[i]) + "".join((fonT[42])[i]) + "".join((fonT[48])[i]) + "".join((fonT[49])[i]) + "".join((fonT[50])[i]))
print("\n")
for i in range(5):
    print("".join((fonT[51])[i]) + "".join((fonT[52])[i]))
while True:
    letters = input("Say something: ")
    if len(letters) == 0:
        while len(letters) == 0:
            letters = input("Say something: ")
    letter_list = []
    for i in range(len(letters)):
        #print(ord(letters[i]))
        if letters[i].isalpha() == True:
            if letters[i].isupper() == True:
                letter_list.append(ord((letters[i]).lower()) - 86)
            else:
                letter_list.append(ord(letters[i]) - 86)
        elif letters[i].isdigit() == True:
            letter_list.append(ord(letters[i]) - 48)
        elif letters[i] == "!":
            letter_list.append(ord(letters[i]) + 4)
        elif letters[i] == ":":
            letter_list.append(ord(letters[i])-20)
        elif letters[i] == " ":
            letter_list.append(ord(letters[i])+15)
        elif letters[i] == "=":
            letter_list.append(ord(letters[i]) - 16)
        elif letters[i] == "?":
            letter_list.append(ord(letters[i]) - 15)
        elif letters[i] == "[":
            letter_list.append(ord(letters[i]) - 42)
        elif letters[i] == "]":
            letter_list.append(ord(letters[i]) - 43)
        elif letters[i] == "<":
            letter_list.append(ord(letters[i]) - 9)
        elif letters[i] == ">":
            letter_list.append(ord(letters[i]) - 10)
        else:
            if letters[i].isalpha() == False:
                letter_list.append(ord(letters[i]))
    jerry = []
    for i in range(5):
        jerry.append("".join((fonT[letter_list[0]])[i]))
        for j in range(len(letter_list) - 1):
            jerry.append("".join((fonT[letter_list[j + 1]])[i]))
        jerry.append("\n")
    print("".join((jerry)))
input()