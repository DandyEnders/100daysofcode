import random
import art
print(art.logo)
print("Welcom to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
  attempts = 5
else:
  attempts = 10

solution = random.randint(1, 100)
is_win = False
while attempts > 0:
  print(f"You have {attempts} remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > solution:
    print("Too high.")
  elif guess == solution:
    print(f"You got it! The answer was {solution}.")
    is_win = True
    attempts = -1
  else:
    print("Too low.")
  
  attempts -= 1
  if attempts > 0 and not is_win:
    print("Guess again.")

if not is_win:
  print("You've run out of guesses. You lose.")
