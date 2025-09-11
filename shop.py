import random
random_num = random.randint(0, 100)
objectlist = ["spoon", "bed", "microwave", "phone", "potato", "bag", "fully grown man", "desk", "toothbrush", "used burger", "Don't buy this omg Dude please no", "yo gurt", "broken in half plastic spork", "nothing", "funny cat pictures"]
random_object = random.choice(objectlist)
print(str("You can buy a " + str(random_object) + str(" for $") + str(random_num) + str(".")))
the_choice = input("Will you?\nType y for Yes, n for No.\n")
if the_choice == "y":
    with open("choice.txt", "w") as f:
        f.write(str("You bought a ") + str(random_object) + (" for $" + str(random_num) + str(".")))
else:
    with open("choice.txt", "w") as f:
        f.write(str("You bought nothing. Wow."))
input("\nPress enter to exit.\n")