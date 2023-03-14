from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

while True:
    choice = input(f"Choose a drink: {menu.get_items()}\n")
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

