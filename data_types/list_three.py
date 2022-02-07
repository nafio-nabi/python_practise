days = []

print(days)

for i in range(7):
    user_input = input("Day: ")
    days.append(user_input)

print(days)

last_day = days.pop()

print(days)
print(last_day)