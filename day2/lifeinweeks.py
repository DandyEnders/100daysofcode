age = input("What is your current age?")

assert int(age) <= 90, "You live too much!"
assert int(age) > 0, "You should born first."

life_expectancy = 90

life_remaining = life_expectancy - int(age)

days = life_remaining * 365
weeks = life_remaining * 52
months = life_remaining * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")