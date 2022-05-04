import os
import random
import logo

card_type = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_screen() -> None:
  os.system("clear") if os.name == "posix" else os.system("cls")


def current_score(hand: list) -> int:
  if sum(hand) > 21 and 11 in hand:
    hand.remove(11)
    hand.append(1)
  return sum(hand)


def deal_card(hand: list, n: int) -> None:
  for _ in range(n):
    hand.append(random.choice(card_type))


def get_judgement(player_score: int, computer_score: int) -> None:
  if player_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if player_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 21:
    return "Lose, opponent has Blackjack 😱"
  elif player_score == 21:
    return "Win with a Blackjack 😎"
  elif player_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif player_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


if __name__ == "__main__":
  clear_screen()
  while True:
    question = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    is_play = input(question).lower() == "y"

    if not is_play:
      exit(0)

    clear_screen()
    print(logo.logo)

    player_hand = []
    computer_hand = []

    deal_card(player_hand, 2)
    deal_card(computer_hand, 1)

    is_user_asking_more_card = True
    while current_score(player_hand) < 21 and is_user_asking_more_card:
      print(
          f"   Your cards: {player_hand}, current score: {current_score(player_hand)}")
      print(f"   Computer's first card: {computer_hand[0]}")

      is_user_asking_more_card = input(
          "Type 'y' to get another card, type 'n' to pass: ").lower() == 'y'
      if is_user_asking_more_card:
        deal_card(player_hand, 1)

    while current_score(computer_hand) < 17:
      deal_card(computer_hand, 1)

    print(
        f"   Your final hand: {player_hand}, final score: {current_score(player_hand)}")
    print(
        f"   Computer's final hand: {computer_hand}, final score: {current_score(computer_hand)}")

    print(get_judgement(current_score(player_hand), current_score(computer_hand)))
