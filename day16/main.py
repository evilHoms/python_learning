from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

menu = Menu()
coffee_maker = CoffeeMaker()
money_maching = MoneyMachine()

def welcome():
    print("Coffe machine v0.1.0")
    return input(f"Do you wanna some coffee? ({menu.get_items()}report): ")

def handle_command(command):
    if command == "report":
        coffee_maker.report()
        money_maching.report()
    else:
        drink = menu.find_drink(command)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_maching.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print("Not enought res")
        else:
            print("Not correct command")

system("clear")      
while True:
    command = welcome()
    system("clear")
    handle_command(command)
    