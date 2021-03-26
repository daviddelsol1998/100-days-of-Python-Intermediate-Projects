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

# variable that holds the amount of money the machine has
money_earned = 0


# TODO 11: Calculate resources, return true if enough else return false
def calc_resources(action_given):
    needs = MENU[action_given]['ingredients']
    enough_materials = False
    for ingredient in needs:
        if needs[ingredient] <= resources[ingredient]:
            enough_materials = True
    return enough_materials


# TODO 12: collect coins
def collect_coins():
    print('Please insert coins.')
    coins_given = {'quarters': int(input('how many quarters?: ')) * 0.25,
                   'dimes': int(input('how many dimes: ')) * 0.10, 'nickles': int(input('how many nickles: ')) * 0.05,
                   'pennies': int(input('how many nickles: ')) * 0.01}
    return coins_given


# TODO 7: Process coins
def process_coins(action_given):
    cost = MENU[action_given]['cost']
    coins_given = collect_coins()

    total = 0

    for coin in coins_given:
        total += coins_given[coin]

    if total < cost:
        print('Sorry, that is not enough money, money returned')
        return 0
    elif total > cost:
        change = round((total - cost),2)
        print(f'Here is ${change} in change.')
        return total - change
    else:
        return total


# TODO 9: Make Coffee
def make_coffee(action_given):
    needs = MENU[action_given]['ingredients']
    for ingredient in needs:
        resources[ingredient] -= needs[ingredient]
    print(f'Here is your {action_given} ☕ Enjoy!')


# TODO 3: Call machine_work() to put everything together
def machine_work(action_given):
    is_enough = calc_resources(action_given)
    if is_enough:
        global money_earned
        global action_completed
        money_earned += process_coins(action_given)
        if money_earned > 0:
            make_coffee(action_given)
            action_completed = True
        else:
            action_completed = True
    else:
        print("Sorry, we don't have enough ingredients to do this.")
        action_completed = True


# variable to check if the unit is ON
is_on = True
action_completed = False

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while is_on:
    action = input('\tWhat would you like? (espresso/latte/cappuccino): ')
    # TODO 2: Check the user’s input to decide what to do next
    # TODO 4: Turn off the Coffee Machine by entering “off” to the prompt.
    if action == 'off':
        is_on = False
    #   TODO 5: Print report
    elif action == 'report':
        for resource in resources:
            if resource == 'coffee':
                print(f'{resource}: {resources[resource]}g')
            else:
                print(f'{resource}: {resources[resource]}ml')
        print(f'money earned: ${round(money_earned,2)}')
    else:
        machine_work(action)

    # TODO 10: The prompt should show every time action has completed
    if action_completed:
        continue
