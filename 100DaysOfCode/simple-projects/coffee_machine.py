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


def count_money():
    quarters = int(input("How man quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_dollars = (quarters * 25 + dimes * 10 + nickles * 5 + pennies * 1) / 100
    return total_dollars


def give_change_and_make_coffee(total_dollars, coffee_type, money):
    if coffee_type == "espresso":
        coffee_price = MENU["espresso"]["cost"]
        coffee_ingredients = MENU["espresso"]["ingredients"]
        if total_dollars < coffee_price:
            print("You didn't insert enough coins. You are refunded")
        elif total_dollars == coffee_price:
            # could have used a for loop to loop through the coffee ingredients
            # and deduct from resources ONLY the item that exist in coffee_ingredients
            resources["water"] -= coffee_ingredients["water"]
            # resources["milk"] -= coffee_ingredients["milk"]
            resources["water"] -= coffee_ingredients["water"]
            money += coffee_price
            print(f"Here is your {coffee_type}")
            return money
        else:
            change = round(total_dollars - coffee_price, 2)
            resources["water"] -= coffee_ingredients["water"]
            # resources["milk"] -= coffee_ingredients["milk"]
            resources["coffee"] -= coffee_ingredients["coffee"]
            money += coffee_price
            print(f"Here is ${change} in change")
            print(f"Here is your {coffee_type}! Have a great day!")
            return money
    elif coffee_type == "latte":
        coffee_price = MENU["latte"]["cost"]
        coffee_ingredients = MENU["latte"]["ingredients"]
        if total_dollars < coffee_price:
            print("You didn't insert enough coins. You are refunded")
        elif total_dollars == coffee_price:
            resources["water"] -= coffee_ingredients["water"]
            resources["milk"] -= coffee_ingredients["milk"]
            resources["water"] -= coffee_ingredients["water"]
            money += coffee_price
            print(f"Here is your {coffee_type}")
            return money
        else:
            change = round(total_dollars - coffee_price, 2)
            resources["water"] -= coffee_ingredients["water"]
            resources["milk"] -= coffee_ingredients["milk"]
            resources["coffee"] -= coffee_ingredients["coffee"]
            money += coffee_price
            print(f"Here is ${change} in change")
            print(f"Here is your {coffee_type}! Have a great day!")
            return money
    elif coffee_type == "cappuccino":
        coffee_price = MENU["cappuccino"]["cost"]
        coffee_ingredients = MENU["cappuccino"]["ingredients"]
        if total_dollars < coffee_price:
            print("You didn't insert enough coins. You are refunded")
        elif total_dollars == coffee_price:
            resources["water"] -= coffee_ingredients["water"]
            resources["milk"] -= coffee_ingredients["milk"]
            resources["water"] -= coffee_ingredients["water"]
            money += coffee_price
            print(f"Here is your {coffee_type}")
            return money
        else:
            change = round(total_dollars - coffee_price, 2)
            resources["water"] -= coffee_ingredients["water"]
            resources["milk"] -= coffee_ingredients["milk"]
            resources["coffee"] -= coffee_ingredients["coffee"]
            money += coffee_price
            print(f"Here is ${change} in change")
            print(f"Here is your {coffee_type}! Have a great day!")
            return money


make_coffee = True
money = 0
while make_coffee:
    user_input = input("What would you like?(Espresso/Latte/Cappuccino): ")
    if user_input == "report":
        print(f" Water: {resources['water']}ml")
        print(f" Milk: {resources['milk']}ml")
        print(f" Coffee: {resources['coffee']}g")
        print(f" Money: ${money}")
    elif user_input.lower() == "espresso":
        # should have created a function is_enough_resource and
        # use a for loop to go through the ingredients dictionary
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and \
                resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            print("Please insert coins")
            total_dollars = count_money()
            money = give_change_and_make_coffee(total_dollars, user_input.lower(), money)
        else:
            print("Sorry out of stock")
    elif user_input.lower() == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and \
                resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            print("Please insert coins")
            total_dollars = count_money()
            money = give_change_and_make_coffee(total_dollars, user_input.lower(), money)
        else:
            print("Sorry out of stock")
    elif user_input.lower() == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and \
                resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Please insert coins")
            total_dollars = count_money()
            money = give_change_and_make_coffee(total_dollars, user_input.lower(), money)
        else:
            print("Sorry out of stock")
    elif user_input.lower() == "off":
        make_coffee = False

# Angela's code. My code is way longer because I didn't understand dictionary very well
"""
profit = 0
def is_resource_sufficient(order_ingredients):
    # Returns True when order can be made, False if ingredients are insufficient.
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    # Returns the total calculated from coins inserted.
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    # Return True when the payment is accepted, or False if money is insufficient.
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    # Deduct the required ingredients from the resources. 
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
"""
