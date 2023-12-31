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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    """Return True when order can be made,False  if insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("sorry, there is not enough{item}")
            return False
        else:
            return True


def process_coins():
    print("please insert coins")
    """Return  the total caculated from coins inserted."""
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennis?:")) * 0.01
    return total


def is_transaction_sucessful(money_received, drink_cost):
    """Return True when the payment is accept,False if money is insufficien"""
    if money_received >= drink_cost:
        change_money = round(money_received - drink_cost, 2)
        print(f"Here is ${change_money} in  change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorrry,that's not enough money.Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True
while is_on:
    choice = input("What would you like?  espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water {resources}['water'] ml")
        print(f"milk {resources}['milk'] ml")
        print(f"coffee {resources}['coffee'] ml")
        print(f"money {profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])




