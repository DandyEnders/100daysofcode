from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_machine_on = True
while is_machine_on:
    user_command = input(f"What would you like? ({m.get_items()})")
    drink_choice = user_command
    if user_command == "off":
        print("The machine is turning off. Good bye!")
        is_machine_on = False
    elif user_command == "report":
        cm.report()
        mm.report()
    elif (drink := m.find_drink(drink_choice)) is not None:
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)
