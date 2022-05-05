# enemies = 1


# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside the function {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # local scopes


# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)


# drink_potion()
# print(potion_strength)

# Global scope

# player_health = 10


# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)


# game()
# print(player_health)

# Python has no block scope
# if a new variable is defined in if statement,
# it can be used outside the if statement.
# (but if inside the if statement was never run,
#  it will cause a syntax error to call variable
#  inside.)
# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton", "Zombie", "Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]

#   print(new_enemy)

# Modifying Global scope

# enemies = 1

# def increase_enemies():
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# global constants

PI = 3.141592
URL = "https//www.google.com"
