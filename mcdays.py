days_passed = int(input("How many days have passed in your Minecraft world? "))
irl_minutes = days_passed * 20
irl_hours = round((irl_minutes * 0.0166667), 2)
irl_days = round((irl_hours * 0.0416667), 2)
print(str(irl_minutes) + " minutes have passed in real life.")
print(str(irl_hours) + " hours have passed in real life.")
print(str(irl_days) + " days have passed in real life.")
input("")