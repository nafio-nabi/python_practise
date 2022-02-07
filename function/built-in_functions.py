user_input_one = input("String: ")
print(user_input_one)

user_input_two = input("Int: ")
try:
    if user_input_two.isdigit:
        user_input_two_int = int(user_input_two)
        print(f"{user_input_two_int}")
except:
    print(f"{user_input_two} is not an integer.")