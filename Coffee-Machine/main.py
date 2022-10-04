# Importing required Data
from Data import MENU, resources

# Extracted required Data
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def resource_update(used_water, used_coffee, used_milk):
    """Updates Resource"""
    global water, coffee, milk
    water -= used_water
    coffee -= used_coffee
    milk -= used_milk
    return coffee, milk, water


def money_taker(dish):
    global money
    """Takes Coin as inputs and calculates total return amount"""
    quaters = (float(input("how many of quarters?: ")) * 25)/100
    dimes = (float(input("how many of dimes?: ")) * 10)/100
    nickles = (float(input("how many of nickles?: ")) * 5)/100
    penny = (float(input("how many of penny?: ")) * 1)/100
    total = quaters + dimes + nickles + penny
    change = (total - MENU[dish]["cost"])

    if total < MENU[dish]["cost"]:
        return "Insufficient Funds hence refunding"
    else:
        print(f"Here is your change ${change}")
        print(f"Enjoy your {dish}")
        resource_update(used_water=MENU[dish]["ingredients"]["water"],
                        used_coffee=MENU[dish]["ingredients"]["coffee"],
                        used_milk=MENU[dish]["ingredients"]["coffee"])
        money += MENU[dish]["cost"]
        return "\n"


def resources_checker(dish):
    """Check if resource is available or not"""
    if water < MENU[dish]["ingredients"]["water"]:
        return f"sorry their is not enough water in machine"
    if coffee < MENU[dish]["ingredients"]["coffee"]:
        return "sorry their is not enough coffee in machine"
    if milk < MENU[dish]["ingredients"]["milk"]:
        return "sorry their is not enough coffee in machine"


def device(dish):
    """The Main Driver Code"""
    global money
    condition = (MENU[dish]["ingredients"]["water"] < water) and\
                (MENU[dish]["ingredients"]["coffee"] < coffee) and \
                (MENU[dish]["ingredients"]["milk"] < milk)
    if condition is True:
        print("Please insert coin.")
        print(money_taker(dish))

    else:
        print(resources_checker(dish))


while True:
    user_input = input("what would you like ? (espresso/latte/cappuccino): ")

    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        device(user_input)

    elif user_input == "report":
        print(f"water : {water} liters")
        print(f"milk : {milk} liters")
        print(f"coffee : {coffee}grams")
        print(f"Money : ${money}")
    elif user_input == "off":
        break

    elif user_input != "espresso" or \
            user_input != "latte" or \
            user_input != "cappuccino" or \
            user_input != "off" or \
            user_input != "report":
        print("invalid input please use valid input")

