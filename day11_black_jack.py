import random
import os

suits = ['hearts', 'spades', 'diamons', 'clubs']
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']
        
def init_deck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append([card, suit])

def print_deck():
    print('''
      _________
     |         |
    ||    |    |
    ||  --|--  |
    ||    |    |
    ||         |
    ||         |
     ==========
    ''')

def print_cards():
    print()


def get_random_card(deck):
    rand_index = random.randint(0, len(deck) - 1)
    return deck.pop(rand_index)

def print_welcome():
    os.system('clear')
    print('BLACK JACK')
    if input('Wanna play? (y/n): ') == 'n':
        quit(0)
        
print_welcome()
deck = init_deck()
my_cards = [get_random_card(deck), get_random_card(deck)]
dealer_cards = [get_random_card(deck), get_random_card(deck)]

print_cards() # Dealer cards
print_deck()
print_cards() # My cards

# TODO ask for more cards
# if no, dealer turn, give cards to dealer, until he will have more then 16 points, after it calculate result
# if yes get one more random cards
# if > 21 auto loose
#
