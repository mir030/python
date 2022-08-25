from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""We need to create object from classes before we can call out the methods from those classes"""
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


machine_on = True
while machine_on:
    user_input = input("What would you like? espresso/latte/cappuccino: ")
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
