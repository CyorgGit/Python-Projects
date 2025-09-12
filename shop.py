import random
random_num = random.randint(0, 100)
if random_num == 0:
    random_num = "free!"
elif random_num == 100:
    random_num = 10000000000000000
# If you haven't, DOWNLOAD THE "shop_list.txt" FILE!
from shop_list import objectlist
random_object = random.choice(objectlist)
print(str("You can buy a " + str(random_object) + str(" for \n\033[92m$") + str(random_num) + str("\033[97m.")))
the_choice = input("\nWill you?\nType Y for Yes, N for No, L to Leave.\n")
if the_choice.lower() == "y":
    if random_object == "Don't buy this omg Dude please no":
        print("\033[101mYou have bought it, despite literally being asked not to.\nYou have exploded the earth, and set the universe into an\neternal loop of emptiness.\n\nAre you proud of yourself?")
        with open("choice.txt", "w") as f:
            f.write(str("You've eternally ruined everything."))
    elif random_object == "kitty!":
        print("\033[95mMeow <(∙ω∙)>")
        with open("choice.txt", "w") as f:
            f.write(str("YOU GOT A KITTYY AWWWWWWWWWW"))
    else:
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
        f.write(str("Not sure what that even means.\nYou should probably write something that counts as a valid answer next time."))
input("\n\033[94mPress enter to exit.\n")
