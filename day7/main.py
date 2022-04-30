import random
import hangman_art
import hangman_words

stages = hangman_art.stages
stages.reverse()
logo = hangman_art.logo
word_list = hangman_words.word_list

print(logo)

chosen_word = random.choice(word_list)
print(f"Pssst, The solution is {chosen_word}")

word_line = ["_"] * len(chosen_word)
hangman_stage = 0

print(word_line)
end_of_game = False
is_player_win = False
while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in word_line:
        print(f"You have already guessed the letter {guess_letter}.\nPlease try another.")

    for i, l in enumerate(chosen_word):
        if l == guess_letter:
            word_line[i] = l

    print(word_line)
    print(stages[hangman_stage])

    if guess_letter not in chosen_word:
        hangman_stage += 1

    if "_" not in word_line:
        end_of_game = True
        is_player_win = True
    if hangman_stage == len(stages):
        end_of_game = True
        is_player_win = False

if is_player_win:
    print("You won!")
else:
    print("You lost...")
