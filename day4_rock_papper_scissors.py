import random

me = int(input('What do you choose? 0 - rock, 1 - papper, 2 - scissors. '))

if me > 2 or me < 0:
    print('Wrong input.')
    exit()
    
opts = ['rock', 'papper', 'scissors']
imgs = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

comp = random.randint(0, 2)
    
print(f'You choose {opts[me]}')
print(imgs[me])
print(f'Computer chooses {opts[comp]}')
print(imgs[comp])

if me == 0 and comp == 2:
    print('Win!')
elif me == 2 and comp == 0:
    print('Loose!')
elif me > comp:
    print('Win!')
elif me < comp:
    print('Loose!')
else:
    print('Draw!')