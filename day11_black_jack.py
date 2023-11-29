import random
import os

score = [0, 0]
suits = ['♥', '♠', '♦', '♣']
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
        
def init_deck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append([card, suit])
    return deck

def print_deck():
    print('''
  -------
||   |   |
|| --|-- |
||   |   |
 ========
    ''')

def print_cards(cards, is_closed):
    for card in cards:
        if is_closed:
            print('''
 -------
|   |   |
| --|-- |
|   |   |
 -------
            ''', end='', flush=True)
        else:
            print(f'''
 -------
| {card[0]}
|   {card[1]}   |
| {card[0]}
 -------
            ''', end='')
    print('')


def get_random_card(deck):
    rand_index = random.randint(0, len(deck) - 1)
    return deck.pop(rand_index)

def print_welcome():
    os.system('clear')
    print('BLACK JACK')
    if input('Wanna play? (y/n): ') == 'n':
        quit(0)
        
def print_all_cards(my, dealer, open_up):
    print_cards(dealer, not open_up)
    print_deck()
    print_cards(my, False)
    
def get_points(cards):
    points = 0
    aces = 0
    for card in cards:
        if card[0] == 'ace':
            points += 11
            aces += 1
        elif card[0] == 'jack' or card[0] == 'queen' or card[0] == 'king' or card[0] == '10':
            points += 10
        else:
            points += int(card[0])
            
    while points > 21 and aces > 0:
        points -= 10
        aces -= 1

    return points

def print_score():
    print(f'You: {score[0]} - Dealer: {score[1]}')
    
def print_table(my, dealer, open_up):
    os.system('clear')
    print_score()
    print_all_cards(my, dealer, open_up)
        
print_welcome()

while True:
    deck = init_deck()
    my_cards = [get_random_card(deck), get_random_card(deck)]
    dealer_cards = [get_random_card(deck), get_random_card(deck)]
    print_table(my_cards, dealer_cards, False)
    
    my_points = get_points(my_cards)
    dealer_points = get_points(dealer_cards)
    
    if my_points == 21 or dealer_points == 21:
        print_table(my_cards, dealer_cards, True)
        print('BLACK JACK!')
        
        if my_points == dealer_points:
            print('Tie!')
        elif my_points == 21:
            print('You WIN!')
            score[0] += 1
        else:
            print('You LOOSE!')
            score[1] += 1

        if input('Wanna play again? (y/n): ') == 'y':
            continue
        else:
            break
        
    not_busted = True
    
    while input('Wanna take another card? (y/n): ' ) == 'y':
        my_cards.append(get_random_card(deck))
        print_table(my_cards, dealer_cards, False)
        my_points = get_points(my_cards)

        if my_points > 21:
            print('BUSTED! You LOOSE!')
            score[1] += 1
            not_busted = False
            break
        elif my_points == 21:
            break
        
    if not_busted:
        while dealer_points < 17:
            dealer_cards.append(get_random_card(deck))
            dealer_points = get_points(dealer_cards)
        
        print_table(my_cards, dealer_cards, True)

        if dealer_points > 21:
            print('Dealer BUSTED! You WIN!')
            score[0] += 1
            not_busted = False
    
    if not_busted:
        if my_points > dealer_points:
            print('You WIN!')
            score[0] += 1
        elif my_points < dealer_points:
            print('You LOOSE!')
            score[1] += 1
        else:
            print('Tie!')
        
    if input('Wanna play again? (y/n): ') == 'y':
        continue
    else:
        break
    
os.system('clear')
print(f'Final score is: {score[0]} - {score[1]}')
print('Good bye!')
