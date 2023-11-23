print("Welcome to Treasure Island. Your mission is to find the threasure.")
action = input("You at a crossroad, where would you like to turn? Type left or right. ")

if action == "right":
    print("You fell into the hole. Game Over")
    exit()
    
if action != "left":
    print("Icorrect input.")
    exit()
    
action = input("You've come to the lake, would you like to wait a boat? Type swim or wait. ")
    
if action == "swim":
    print("You got attacked by an angry monster. Game Over")
    exit()
    
if action != "wait":
    print("Icorrect input.")
    exit()
    
action = input("You see three doors, which one you wanna open? Type red blue or yellow? ")

if action == "red" or action == "blue":
    print("The room is full of fire! Game Over!")
    exit()
    
if action != "yellow":
    print("Icorrect input.")
    exit()
    
print("You've found the treasure! You win!")