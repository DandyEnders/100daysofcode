enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside the function {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

