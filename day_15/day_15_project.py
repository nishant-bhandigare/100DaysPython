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
    "money": 0,
}

# coins = {"penny": 0.01, "nickel": 0.05, "dime": 0.10, "quarter": 0.25,}

def check_money(coffee):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    cost=MENU[coffee]["cost"]
    total = round((quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01), 2)
    reject = "Sorry you don't have enough money. Money Refunded."

    if coffee=="espresso" and total<1.50:
        print(reject)
        return False
    elif coffee=="latte" and total<2.50:
        print(reject)
        return False
    elif coffee=="cappuccino" and total<3.00:
        print(reject)
        return False
    
    change = round((total - cost),2)
    print(f"Here is your ${change} in change.")
    return True
    
def check_resources(coffee):

    if coffee == "espresso":
        if resources["water"] >= MENU[coffee]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
            return True
        print("Not enough resources")
        return False
    else:
        if resources["water"] >= MENU[coffee]["ingredients"]["water"] and resources["milk"] >= MENU[coffee]["ingredients"]["milk"] and resources["coffee"] >= MENU[coffee]["ingredients"]["coffee"]:
            return True
        print("Not enough resources")
        return False

def get_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']}")

def make_espresso():
    if check_resources('espresso') and check_money('espresso'): 
        resources["water"] -= 50
        resources["coffee"] -= 18
        resources["money"] += 1.50
        print("Here is your Espresso Enjoy!")
    

def make_latte():
    if check_resources('latte') and check_money('latte'): 
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
        resources["money"] += 2.50
        print("Here is your Latte Enjoy!")

def make_cappuccino():
    if check_resources('cappuccino') and check_money('cappuccino'): 
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100
        resources["money"] += 3.00
        print("Here is your Cappuccino Enjoy!")


def make_coffee(coffee):
    if coffee == "espresso":
        make_espresso()
    elif coffee == "latte":
        make_latte()
    else:
        make_cappuccino()

def coffee_machine():
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == 'report':
        get_report()
        return
    else:
        make_coffee(coffee)


while True:
    coffee_machine()