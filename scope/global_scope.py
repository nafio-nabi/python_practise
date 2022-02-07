# Variables with global scope. It can be accessed, and modified anywhere in the program.
first_name = "John"
last_name = "Doe"

def print_name():
    return f"{first_name} {last_name}"

print(print_name())