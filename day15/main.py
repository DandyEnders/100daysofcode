MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient_for(input_menu):
    assert input_menu in MENU.keys()

    water, milk, coffee = MENU["input_menu"]["ingredients"].values()
    return resources.water >= water and resources.milk >= milk and resources.coffee >= coffee


def deficient_resources(input_menu) -> list:
    assert input_menu in MENU.keys()

    result = []
    req_water, req_milk, req_coffee = MENU["input_menu"]["ingredients"].values()
    if req_water > resources.water: result.append("water")
    if req_milk > resources.milk: result.append("milk")
    if req_coffee > resources.coffee: result.append("coffee")
    return result


# DONE: do following while dispensing is not finished:
is_machine_on = True
while is_machine_on:
    # DONE: take input("What would you like? (espresso/latte/cappuccino): ")
    user_command = input("What would you like? (espresso/latte/cappuccino): ")
    menu_choice = user_command

    # DONE: if input is "off", terminate dispensing
    if user_command == "off":
        is_machine_on = False
        print("Turning off the coffee machine. Good bye!")

    # DONE: if input is "report", print Water, Milk, Coffee, Money remainders
    #   each in each line
    elif user_command == "report":
        for name, amount in resources.items():
            print(f"{name}: {amount}")

    # DONE: if input is either of the coffee choices,
    #   and if resources are not sufficient,
    #   print "Sorry there is not enough {resource}."
    elif menu_choice in MENU.keys() and not is_resources_sufficient_for(menu_choice):
        print(f"Sorry there is not enough {', '.join(deficient_resources(menu_choice))}.")

    # DONE: if input is either of the coffee choices,
    #   and if resources are sufficient,
    #   ask user for each coin types in each line:
    #   input("Insert coin in the format of: #quarters #dimes #nickles #pennies
    elif menu_choice in MENU.keys() and is_resources_sufficient_for(menu_choice):
        quarter, dime, nickle, penny = input("Insert coin in the format of: #quarters #dimes #nickles #pennies: ")

# TODO: if user did not insert enough money,
#   print("Sorry that's not enough money. Money refunded.")
# TODO: if user did insert enough money,
#   reflect money input into amount of money remaining
# TODO: if user inserted too much money, offer the change
#   print("Here is ${amount:.2f} dollars in change.")
# TODO: if the coffee transaction was successful,
#   deduct the amount of water, milk and coffee from resource
#   then, print("Here is your {choice}. Enjoy!")
