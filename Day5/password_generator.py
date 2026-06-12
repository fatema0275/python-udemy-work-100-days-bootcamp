import random;
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# The first half of the solution generates the password following a order i.e. letters followed by numbers then followed by special characters.
# Which is improved in second half of the solution.
generated_password = ""

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    generated_password = generated_password + random_char

for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    generated_password = generated_password + random_num

for sym in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    generated_password = generated_password + random_symbol

print("Generated Password: ", generated_password)

# Improved Version:

generated_password = []

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    generated_password.append(random_char)

for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    generated_password.append(random_num)

for sym in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    generated_password.append(random_symbol)

pwd = ""
random.shuffle(generated_password)
for i in generated_password:
    pwd += i

print("Your password is: ", pwd)
