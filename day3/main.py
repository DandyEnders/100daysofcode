print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rolldercoaster!")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $12")
  elif age <= 12:
    print("Please apy $7")
  else:
    print("Please pay $5")
else:
  print("Sorry, you have to grow taller before you can ride.")
