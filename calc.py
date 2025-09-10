import random
digits = input("What numbers should the\nrandomly generated numbers be?\n")
if digits.isnumeric() == False:
    print("Dude.")
digital = int(digits)
random_num = random.randint(-1 * digital, 1 * digital)
test_thing = input("Say a number.\n")
if test_thing.isnumeric() == False:
    print("Dude.")
other_thing = int(test_thing)
print(str("Your number is " + str(other_thing)) + str(", plus a randomly generated number, ") + str(random_num) + str(".") + str("\nWhen added together, it makes ") + str(other_thing + random_num) + str(".") + str("\nWow, what a cool number."))
with open("awesome.txt", "w") as f:
    f.write(str("Chosen randomly generated numbers range:\n") + str(digits) + str("\nRandom number:\n") + str(random_num) + str("\nChosen number:\n") + str(test_thing) + str("\nNumbers added together:\n") + str(other_thing + random_num))
input("\nPress enter to exit.\n")
