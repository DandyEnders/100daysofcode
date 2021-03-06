# Review:
# Create a function called greet().
# Write 3 print statements inside the funciton.
# Call the greet () function and run your code.

def greet():
  print("Hello!")
  print("How are you?")
  print("I am fine, thank you.")

greet()

def greet_with_name(name):
  print(f"Hello {name}!")
  print(f"How do you do {name}?")

greet_with_name("Jack")

def greet_with(name, location):
  print(f"Hello {name}.")
  print(f"What is it like in {location}?")

greet_with("Jack", "Nowhere")

def greet_with(name="Jack", location="London"):
  print(f"Hello {name}.")
  print(f"What is it like in {location}?")

greet_with()