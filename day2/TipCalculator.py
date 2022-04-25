print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage_tip = input("What is the percentage of tips: 10, 12, 15? ")
n_people = input("How many people to split the bill? ")
personal_tip = float(total_bill) / int(n_people) * (1 + int(percentage_tip) / 100)
print(f"Each person should pay: ${round(personal_tip, 2):.2f}")


