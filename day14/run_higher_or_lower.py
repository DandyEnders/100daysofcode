import os
import random
from art import logo, vs
from game_data import data

def is_first_not_loser(A, B) -> bool:
  return A["follower_count"] >= B["follower_count"]

def print_versus(A, B) -> None:
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

def clear_screen() -> None:
  os.system("clear") if os.name == "posix" else os.system("cls")

if __name__ == "__main__":

  score = 0
  is_game_running = True
  contenderB = random.choice(data)
  print(logo)
  while is_game_running:
    contenderA = contenderB
    contenderB = random.choice(data)

    print_versus(contenderA, contenderB)

    player_choice = input("Who has more Followers? Type 'A' or 'B': ").lower()
    
    is_player_correct = (is_first_not_loser(contenderA, contenderB)) == (player_choice == "a")
    
    if is_player_correct:
      score += 1
      clear_screen()
      print(logo)
      print(f"You're right! Current score: {score}") 
    else:
      clear_screen()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      is_game_running = False

    