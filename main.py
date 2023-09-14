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
    "coffee": 100
}


def report():
    # prints report of remaining resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")
    return


def check_resource(order_ingredients):
    # checks enough resources exist for drink
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_money():
    # returns the total amount the guest paid
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_funds(money_received, cost):
    # checks if there is enough money
    if money_received >= cost:
        change = round(money_received - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    # deducts amount from resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


program_on = True

while program_on:
    guest_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if guest_choice == "off":
        program_on = False
    elif guest_choice == "report":
        report()
    else:
        drink = MENU[guest_choice]
        if check_resource(drink["ingredients"]):
            payment = process_money()
            if check_funds(payment, drink["cost"]):
                make_drink(guest_choice, drink["ingredients"])