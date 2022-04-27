import random
names_string = input("Give me everybody's names, seprated by a comma. ")
names = names_string.split(", ")

print(f"The person to pay the bill is: {random.choice(names)}")