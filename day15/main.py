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
    "money": 0.0,
}


def is_resources_sufficient_for(input_menu):
    assert input_menu in MENU.keys()

    for ingredient, cost in MENU[input_menu]["ingredients"].items():
        if resources[ingredient] < cost:
            return False
    return True


def deficient_resources(input_menu) -> list:
    assert input_menu in MENU.keys()

    result = []
    for ingredient, cost in MENU[input_menu]["ingredients"].items():
        if resources[ingredient] < cost:
            result.append(ingredient)
    return result


def is_money_sufficient_for(input_menu, money_paid) -> bool:
    assert is_resources_sufficient_for(input_menu)

    return MENU[input_menu]["cost"] <= money_paid


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
        quarter, dime, nickle, penny = int(quarter), int(dime), int(nickle), int(penny)
        money_total = quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01

        # DONE: if user did not insert enough money,
        #   print("Sorry that's not enough money. Money refunded.")
        if not is_money_sufficient_for(menu_choice, money_total):
            print("Sorry that's not enough money. Money refunded.")

        # DONE: if user did insert enough money,
        #   reflect money input into amount of money remaining
        else:
            resources["money"] -= MENU[menu_choice]["cost"]

            # DONE: if user inserted too much money, offer the change
            #   print("Here is ${amount:.2f} dollars in change.")
            change = money_total - MENU[menu_choice]["cost"]
            if change > 0:
                print(f"Here is ${change:.2f} dollars in change.")

            # DONE: if the coffee transaction was successful,
            #   deduct the amount of water, milk and coffee from resource
            #   then, print("Here is your {choice}. Enjoy!")
            print(f"Here is your {menu_choice}. Enjoy!")
