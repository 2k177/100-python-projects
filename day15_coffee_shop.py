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

coffee_machine_resource = {
    "water" : 100,
    "milk" : 50,
    "coffee" : 76,
    "money" : 2.5
}

def check_resource(drink):
    for item in drink:
        if coffee_machine_resource[item] - drink[item] < 0:
            return False
    return True

def check_balance(drink):
    if coffee_machine_resource["money"] - drink < 0:
        return False
    return True

def prepare_coffee_with_coffe_ingredient(drink_name, drink):
    for item in drink:
        coffee_machine_resource[item] -= drink[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def payment_transaction(money_received, drink_cost):
    return drink_cost - money_received

def print_report():
    print(f"Water: {coffee_machine_resource['water']}ml")
    print(f"Milk: {coffee_machine_resource['milk']}ml")
    print(f"Coffee: {coffee_machine_resource['coffee']}g")
    print(f"Money: ${coffee_machine_resource['money']}")

user_choice = input("What would you like? (espresso/latte/cappuccino)")
if user_choice.lower() == "report":
    print_report()
else:
    drink = MENU[user_choice]
    check_resource(drink["ingredients"])
    check_balance(drink["cost"])
    print("this order is getting prepared...")
    prepare_coffee_with_coffe_ingredient(user_choice, drink["ingredients"])
    coffee_machine_resource["money"] = payment_transaction(drink["cost"], coffee_machine_resource["money"])
    print_report()
