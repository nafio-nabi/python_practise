from datetime import datetime

# Get user's date of birth.
user_input = input("Enter your date of birth in the format: dd/mm/yy: ")
user_date_of_birth = datetime.strptime(user_input, "%d/%m/%Y")

# Get current date.
current_date = datetime.today()

# Calculate age.
user_age = current_date - user_date_of_birth

# Print user's age.
years = user_age.days // 365
print(f"Your age is {years} years.")