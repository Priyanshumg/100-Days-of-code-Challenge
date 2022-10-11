from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from MoneyMachine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have? ({options})")
    drink = menu.find_drink(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


