import time
s = input("Type something! ")
s1 = 0
s2 = len(s)
while True:
    for i in range(s2):
        print(s[s1:s2])
        s1 = s1 + 1
        time.sleep(0.01)
    s1 = len(s) - 1
    for i in range(s2):
        print(s[s1:s2])
        s1 = s1 - 1
        time.sleep(0.01)
    s1 = 0
