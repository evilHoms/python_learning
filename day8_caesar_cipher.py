alphabet = [
    'a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z'
]

def crypt(word, shift, action):
    res = ''
    for char in word:
        if not char in alphabet:
            res += char
            continue
        
        index = alphabet.index(char)
        
        if action == 'encrypt':
            shifted_index = index + shift
        else:
            shifted_index = index - shift
            
        shifted_index = shifted_index % len(alphabet)
        res += alphabet[shifted_index]
        
    return res

while True:
    action = input('Type \'encrypt\' or \'decrypt\': ')
    if action != 'encrypt' and action != 'decrypt':
        break
    word = input('Type the word: ')
    shift = int(input('Type the shift number: '))
    
    print(crypt(word, shift, action))
    