import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")

# Taking inputs from the User
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty list to store characters
password_list = []

# Add specified number of random letters to the list
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add specified number of random symbols to the list
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add specified number of random numbers to the list
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the list to ensure randomness
random.shuffle(password_list)

# Join the characters to create the password
password = ''.join(password_list)

# Shuffle the password string again to create a new string
shuffled_password_list = list(password)
random.shuffle(shuffled_password_list)
shuffled_password = ''.join(shuffled_password_list)

print("Your securely generated Password is:", shuffled_password)
