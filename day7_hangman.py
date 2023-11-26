import random
import os

lives_imgs = ['''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
===========
''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
===========
''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
===========
''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
===========
''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
===========
''', '''
   +---+
   |   |
   O   |
       |
       |
       |
===========
''', '''
   +---+
   |   |
       |
       |
       |
       |
===========
''']

words = ['test', 'cat', 'house']

word = random.choice(words)

shown_word = []
lives_left = 6

for letter in word:
    shown_word.append('_')

while '_' in shown_word and lives_left != 0:
    print(''.join(shown_word))
    print(lives_imgs[lives_left])
    char = input('Guess a letter: ').lower()

    is_guessed_correctly = False
    for index, letter in enumerate(word):
        if letter == char:
            shown_word[index] = letter
            is_guessed_correctly = True
            
    if not is_guessed_correctly:
        lives_left -= 1
        
    os.system('cls' if os.name == 'nt' else 'clear')

print('Answer is: ' + ''.join(word))
print(lives_imgs[lives_left])    
if lives_left > 0:
    print('You win!')
else:
    print('Game Over. You loose!')
            