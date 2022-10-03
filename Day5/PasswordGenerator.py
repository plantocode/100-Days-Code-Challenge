#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
import random

random_letters = ""
for n in range (1,(nr_letters + 1)):
  random_letters += (random.choice(letters))

random_symbols = ""
for n in range (1,(nr_symbols + 1)):
  random_symbols += (random.choice(symbols))

random_numbers = ""
for n in range (1,(nr_numbers + 1)):
  random_numbers += (random.choice(numbers))

random_password = random_letters + random_symbols + random_numbers
print(random_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = list(random_password)

random.shuffle(random_password)

random_hard_password = ""
for character in random_password:
  random_hard_password += character

print(random_hard_password)
