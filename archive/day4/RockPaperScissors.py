import random

try: 
  choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")) 
  if not (0 <= choice <= 2): 
    print("Your answer is invalid, You lose!")
    exit(0)
except ValueError:
  print("Your answer is invalid, You lose!")
  exit(0)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_list = [rock, paper, scissors]
computer = random.randint(0, 2)

print(f"You played:\n{rps_list[choice]}")
print(f"Computer chose:\n{rps_list[computer]}")

if choice == computer:
  print("A tie!")
elif choice == 0 and computer == 1 \
  or choice == 1 and computer == 2 \
  or choice == 2 and computer == 0:
    print("You lose!")
else:
  print("You win!")
