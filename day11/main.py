import os


def clear_screen():
    os.system("clear") if os.name == "posix" else os.system("cls")


if __name__ == "__main__":
    while True:
        clear_screen()
        question = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
        is_play = input(question).lower() == "y"

        if not is_play:
            exit(0)
