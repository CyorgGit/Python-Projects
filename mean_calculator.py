amount = 0
current = 0
total = 0
mean = 0

amount = int(input("How many numbers do you have in your list? "))
for i in range(amount):
    current = int(input(str("#") + str(i) + str(": ")))
    total = total + current
mean = total / amount
print(mean)
input()