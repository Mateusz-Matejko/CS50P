# Ask user for their name
name = input("What's your name? ")

# Remove withespace from str and capitalize user's name
name = name.strip().title()

# Say hello to the user
print(f"hello, {name}")