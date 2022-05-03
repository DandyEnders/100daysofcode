import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bidder_dict = {}
is_other_bidding = True

while is_other_bidding: 
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  
  bidder_dict[name] = bid
  
  is_other_bidding = True if input("Is there other person bidding? Y/N ").lower() == "y" else False
  os.system('cls' if os.name=='nt' else 'clear')
  
cur_highest_bid = -1
highest_bidder = ""
for key in bidder_dict:
  if cur_highest_bid < bidder_dict[key]:
    highest_bidder = key
    cur_highest_bid = bidder_dict[key]
    
print(f"The highest bidder is {highest_bidder} with ${cur_highest_bid}.")