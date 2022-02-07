# first_name, and last_name are variables with local scope. They can only be accessed, and modfied in the functions they are defined.
def print_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(print_name("John", "Doe"))
# error
# print(f"{first_name} {last_name}")