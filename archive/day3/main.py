print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rolldercoaster!")
  age = int(input("What is your age? "))
  bill = 0
  
  if 45 <= age <= 55:
    print("Everything is going to be ok. Have a free rid on us!")
  elif age >= 18:
    bill = 12
    print("Please pay $12")
  elif age >= 12:
    bill = 7
    print("Please apy $7")
  else:
    bill = 5
    print("Please pay $5")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}.")
    
else:
  print("Sorry, you have to grow taller before you can ride.")
