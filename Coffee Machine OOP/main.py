from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

# todo prompt user
while is_on:
    action = input(f'What would you like? {menu.get_items()}: ').lower()
    if action == 'off':
        is_on = False
    elif action == 'report':
        # todo print report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(action)
        # todo check if resources are sufficient, if they are then make coffee
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_enough_money = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_enough_money:
            coffee_maker.make_coffee(drink)
