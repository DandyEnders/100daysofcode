#Password Generator Project
from posixpath import split
import random
from secrets import choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


result = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(nr_letters):
  result += random.choice(letters)

for i in range(nr_symbols):
  result += random.choice(symbols)

for i in range(nr_numbers):
  result += random.choice(numbers)
print(f"Your password is : {result}")

aux = ""
choices_left = {}
if nr_letters > 0:
  choices_left["letter"] = nr_letters
if nr_symbols > 0:
  choices_left["symbol"] = nr_symbols
if nr_numbers > 0:
  choices_left["number"] = nr_numbers

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for _ in range(nr_letters + nr_symbols + nr_numbers):
  
  turn = random.choice(tuple(choices_left.keys()))
  choices_left[turn] -= 1
  if choices_left[turn] <= 0:
    choices_left.pop(turn)
  
  if turn == "letter":
    aux += random.choice(letters) 
  elif turn == "symbol":
    aux += random.choice(symbols) 
  elif turn == "number":
    aux += random.choice(numbers) 
    
print(random.shuffle(list(result.split())))
print(f"Your password is : {aux}")
split_result = list(result)
random.shuffle(split_result)
print(f"Your password is : {''.join(split_result)}")
