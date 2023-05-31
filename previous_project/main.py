import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
temp = 0

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# total_length = nr_numbers + nr_letters + nr_symbols

# while nr_symbols > 0:
#     number = random.randint(0, len(symbols))
#     password.insert(temp, symbols[number])
#     temp += 1
#     nr_symbols -= 1
#
# while nr_letters > 0:
#     number = random.randint(0, len(letters))
#     password.insert(temp, letters[number])
#     temp += 1
#     nr_letters -= 1
#
# while nr_numbers > 0:
#     number = random.randint(0, len(numbers))
#     password.insert(temp, numbers[number])
#     temp += 1
#     nr_numbers -= 1
#
# finish = ''.join(password)
#
# print(f"Your generated password is {finish}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

while nr_symbols > 0:
    password.insert(temp, random.choice(symbols))
    temp += 1
    nr_symbols -= 1

while nr_letters > 0:
    password.insert(temp, random.choice(letters))
    temp += 1
    nr_letters -= 1

while nr_numbers > 0:
    password.insert(temp, random.choice(numbers))
    temp += 1
    nr_numbers -= 1

random.shuffle(password)

finish = ''.join(password)

print(f"Your generated password is {finish}")



