from pathlib import Path

dir = Path(__file__).parent.resolve()

names_file_path = f'{dir}/Input/Names/invited_names.txt'
letter_file_path = f'{dir}/Input/Letters/starting_letter.txt'

with open(names_file_path) as file:
    names = file.readlines()
    
with open(letter_file_path) as file:
    template = file.read()
    
for name in names:
    sname = name.strip()
    letter = template.replace('[name]', sname)
    with open(f'{dir}/Output/ReadyToSend/letter_for_{sname}.txt', 'w') as file:
        file.write(letter)
    

