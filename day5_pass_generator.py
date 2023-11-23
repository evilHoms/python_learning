import random

print('Welcom to python password generator')
pass_len = int(input('How many characters would you like in your password? 8 - 20 characters usually the best option, 4 characters minimum. Type a number. '))

if pass_len < 4:
    print('Too short password!')
    exit()

add_symbols = str(input('Would you like to include symbols to the password? Type \'Y\' or \'N\'. '))

char_number = [1, 1, 1] # lower letter, upper letters, numbers

if add_symbols.lower() == 'y':
    char_number.append(1) # add symbols

for num in range(len(char_number), pass_len):
    rnd_index = random.randint(0, len(char_number) - 1)
    char_number[rnd_index] += 1

lower_chars = []
for value in range(97, 123):
    lower_chars.append(chr(value))
    
upper_chars = []
for value in range(65, 91):
    upper_chars.append(chr(value))
    
number_chars = []
for value in range(0, 10):
    number_chars.append(str(value))
    
symbol_chars = ['!', '#', '$', '(', ')', '%', '&', '*', '+']
    
result = []

for char in range(0, pass_len):
    group_index = 0
    while char_number[group_index] == 0:
        group_index += 1
        
    char_number[group_index] -= 1
    rnd_char = ''

    if group_index == 0:
        result.append(random.choice(lower_chars))
    elif group_index == 1:
        result.append(random.choice(upper_chars))
    elif group_index == 2:
        result.append(random.choice(number_chars))
    elif group_index == 3:
        result.append(random.choice(symbol_chars))
    
random.shuffle(result)
result = ''.join(result)

print(f'Your password is: {result}')
