import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Pssst, The solution is {chosen_word}")

word_line = ["_"] * len(chosen_word)

print(word_line)

guess_letter = input("Guess a letter: ").lower()

for i, l in enumerate(chosen_word):
  if l == guess_letter:
    word_line[i] = l
    
print(word_line)