age_string = input("What is your age?\n")
age_int = int(age_string)

if age_int >= 18:
    print("You can get on the roller-coaster, and the bumper car.")
elif age_int >= 10 and age_int < 18:
    print("You can't get on the roller-coaster. However, you can get on the bumper car.")
else:
    print("You are not old enough to get on any of the rides.")