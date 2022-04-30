import random


word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess_letter = input("Guess a letter: ")

for l in chosen_word:
  if l == guess_letter:
    print(True)
  else:
    print(False)