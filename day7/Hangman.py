import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stages.reverse()

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Pssst, The solution is {chosen_word}")

word_line = ["_"] * len(chosen_word)
hangman_stage = 0

print(word_line)
end_of_game = False
is_player_win = False
while not end_of_game:
  guess_letter = input("Guess a letter: ").lower()

  for i, l in enumerate(chosen_word):
    if l == guess_letter:
      word_line[i] = l
      
  if guess_letter not in chosen_word:
    hangman_stage += 1
  
  print(word_line)
  print(stages[hangman_stage]) 
  
  
  
  if "_" not in word_line:
    end_of_game = True
    is_player_win = True
  if hangman_stage == len(stages)-1:
    end_of_game = True
    is_player_win = False

if is_player_win:
  print("You won!")
else:
  print("You lost...")