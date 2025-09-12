import random
import os
os.system('')
random_num = random.randint(0, 100)
if random_num == 0:
    random_num = "free!"
elif random_num == 100:
    random_num = 10000000000000000
# I should probably like. Make this rely on a .txt file list instead of stuffing all the objects into the code.
objectlist = ["spoon", "bed", "microwave", "phone", "potato", "bag", "fully grown man", "desk", "toothbrush", 
"used burger", "yo gurt", "broken in half plastic spork", "nothing", 
"funny cat pictures", "triangle-shaped pb&j sandwich", "Don't buy this omg Dude please no", "half-eaten chicken nugget", 
"playing card", "unopened carton of chocolate milk", "keychain of a weird animal"]
random_object = random.choice(objectlist)
print(str("You can buy a " + str(random_object) + str(" for \n\033[92m$") + str(random_num) + str("\033[97m.")))
the_choice = input("\nWill you?\nType Y for Yes, N for No, L to Leave.\n")
if the_choice.lower() == "y":
    print("You spent your money on a", random_object + str("."))
    with open("choice.txt", "w") as f:
        f.write(str("You bought a ") + str(random_object) + (" for $" + str(random_num) + str(".")))
elif the_choice.lower() == "n":
    print("You chose not to purchase anything.")
    with open("choice.txt", "w") as f:
        f.write(str("You bought nothing. Wow."))
elif the_choice.lower() == "l":
    print("Goodbye!")
    with open("choice.txt", "w") as f:
            f.write(str("You left the shop."))
else:
    with open("choice.txt", "w") as f:
        f.write(str("Not sure what that even means.\nYou should probably write something that counts as a valid answer next time, instead of " + str(the_choice) + str(".")))
input("\n\033[94mPress enter to exit.\n")
