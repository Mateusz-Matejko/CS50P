# Ask user's for their name
name = input("What's your name? ").strip().title()

# Ask user's for their surname
surname = input("What's your surname? ").strip().title()

# chain name and surname together 
Fname = name + surname 

# Say hello to the user
print(f"hello, {name} {surname}")