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
    "capuccino": {
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


# print(MENU['espresso']['cost'])

def calculate_money(money1, money2, money3, money4):
    money1 = 0.25 * money1
    money2 = 0.1 * money2
    money3 = 0.05 * money3
    money4 = 0.01 * money4
    total = money2 + money3 + money4 + money1
    return total


def calculate_resources(coffee):
    temp_drink = MENU[coffee]
    if coffee == 'capuccino' or coffee == 'latte':
        rest_resources = {
            "water": resources["water"] - temp_drink['ingredients']['water'],
            "milk": resources["milk"] - temp_drink['ingredients']['milk'],
            "coffee": resources["coffee"] - temp_drink['ingredients']['coffee'],
        }
    else:
        rest_resources = {
            "water": resources["water"] - temp_drink['ingredients']['water'],
            "milk": temp_resources["milk"],
            "coffee": resources["coffee"] - temp_drink['ingredients']['coffee'],
        }
    return rest_resources


while resources["water"] > 0 and resources["milk"] > 0 and resources["coffee"] > 0:
    choice = input("What coffee do you want? espresso ($1.5), latte ($2.5), capuccino ($3.0): ")

    quarters = int(input("How many quarters ($0.25) do you want to insert?: "))
    dimes = int(input("How many dimes ($0.1) do you want to insert?: "))
    nickels = int(input("How many nickels ($0.05) do you want to insert?: "))
    pennies = int(input("How many pennies ($0.01) do you want to insert?: "))

    total_money = calculate_money(quarters, dimes, nickels, pennies)
    temp_resources = calculate_resources(choice)
    resources = temp_resources

    if resources["water"] <= 0 or resources["milk"] <= 0 or resources["coffee"] <= 0:
        print("We don't have enough resources. Sorry.")
        break
    else:
        if total_money >= MENU[choice]['cost']:
            print(f"You get the {choice} here -> ☕ <-")
            print(f"Here is your change ${round(total_money - MENU[choice]['cost'])}")
        else:
            print("You didn't have enough money. Sorry.")
            continue

    see_resources = input("If you want to see resources we have... Type 'resources'... if not press 'enter': ")

    if see_resources == 'resources':
        print(f"{temp_resources}")
    else:
        continue

