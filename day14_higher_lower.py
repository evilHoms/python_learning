from day14_data import data
from os import system
from random import randint
from copy import deepcopy

system('clear')

while True:
    print('Higher Lower')
    
    round_data = deepcopy(data)

    if input('Wanna play? (y/n): ') == 'n':
        break
    
    items = [
        round_data.pop(randint(0, len(round_data) - 1)),
        round_data.pop(randint(0, len(round_data) - 1)),
    ]
    
    score = 0
    system('clear')
    
    while True:
        correct_ans = '1' if items[0]['follower_count'] > items[1]['follower_count'] else '2'
        
        print(f'1) {items[0]["name"]}, {items[0]["description"]}')
        print('vs')
        print(f'2) {items[1]["name"]}, {items[1]["description"]}')
    
        if input('Who has more subscribers? (1/2): ') == correct_ans:
            items[0] = items[int(correct_ans) - 1].copy()
            items[1] = round_data.pop(randint(0, len(round_data) - 1))
            score += 1
            system('clear')
            print(f'Correct, score is: {score}')
            
            if len(round_data) == 0:
                print(score)
                system('Wow, you win, unexpected!')
                break
        else:
            system('clear')
            print(score)
            print(f'1) {items[0]["name"]}: {items[0]["follower_count"]}')
            print(f'2) {items[1]["name"]}, {items[1]["follower_count"]}')
            print('Wrong. You loose.')
            break

