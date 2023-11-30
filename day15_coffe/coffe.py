from menu import menu
from os import system

resources = {
    "water": 600,
    "milk": 500,
    "coffee": 100,
}

def welcome():
    print("Coffe machine v0.0.1")
    return input("Do you wanna some coffe? (latte/cappuchino/espresso/report): ")

def show_report():
    print(resources)
    
def is_enough_res(coffee):
    if (resources["milk"] < menu[coffee]["ingredients"]["milk"]
        or resources["water"] < menu[coffee]["ingredients"]["water"]
        or resources["coffee"] < menu[coffee]["ingredients"]["coffee"]):
        return False
    return True
    
def make_coffee(coffee):
    resources["water"] -= menu[coffee]["ingredients"]["water"]
    resources["milk"] -= menu[coffee]["ingredients"]["milk"]
    resources["coffee"] -= menu[coffee]["ingredients"]["coffee"]
    print(f"Here your hot {coffee}")
    
def take_money(coffee):
    money = 0
    while True:
        print(f"Inserted money: {money}")
        insert = int(input("Insert money (50, 100, 200, 500, 0 to end): "))
        money += insert
        if insert == 0:
            break
        
    if money >= menu[coffee]["price"]:
        print(f"Thank you, here your change: {money - menu[coffee]['price']}p")
        return True
    else:
        print(f"Sorry, not enough money for the {coffee}")
        return False

def handle_command(command):
    if command == "report":
        show_report()
    elif command in menu:
        if is_enough_res(command):
            if take_money(command):
                make_coffee(command)
                print('You are welcome')
            else:
                print("Not enought money")
        else:
            print("Not enought res")
    else:
        print("Not correct command")

system("clear")      
while True:
    command = welcome()
    system("clear")
    handle_command(command)
    