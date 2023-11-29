import os
import random

logo = '''

 _____                        ___    _   _                 _               
|  __ \                      / _ \  | \ | |               | |              
| |  \/_   _  ___  ___ ___  / /_\ \ |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| |  _  | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | | | | | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/ \_| |_/ \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                                                           
                                                                           

'''

os.system('clear')
print(logo)

if input('Wanna play? (y/n): ') == 'n':
    exit(0)

while True:
    os.system('clear')
    
    if input('Choose a mode (easy/hard): ') == 'easy':
        lives = 10
    else:
        lives = 5
        
    secret_num = random.randint(1, 100)
    guess = -1
    
    while secret_num != guess and lives > 0:
        print(f'You have {lives} lives.')
        guess = int(input('Guess a number between 1 and 100: '))
        
        if secret_num > guess:
            print('Too low')
            lives -= 1
        elif secret_num < guess:
            print('Too high')
            lives -= 1
        else:
            print('Correct!')
            
    if secret_num != guess:
        print(f'You loose, secret number was: {secret_num}')
    else:
        print('You WIN!')
        
    if input('Wanna play againt? (y/n): ') == 'n':
        break
