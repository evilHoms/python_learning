import os

print('Auction started!')

comp_dict = {}

while True:
    name = input('Please enter your name: ')
    bet = int(input('Your bet is: $'))
    comp_dict[name] = bet
    is_other_competitor = input('Is there another competitor? (y/n) ')
    if is_other_competitor == 'y':
        os.system('clear')
        continue
    else:
        break

max_bet = -1
winner = ''

for name in comp_dict:
    if comp_dict[name] > max_bet:
        max_bet = int(comp_dict[name])
        winner = name

print(f'The winner is: {winner}, with bet ${comp_dict[winner]}')