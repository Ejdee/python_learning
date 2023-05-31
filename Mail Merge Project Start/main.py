invited_names_right = []

with open('Input/Letters/starting_letter.txt') as letter:
    starting_letter = letter.read()

with open('Input/Names/invited_names.txt') as names:
    invited = names.readlines()

for name in invited:
    invited_names_right.append(name.strip())


for name in invited_names_right:
    new_text = starting_letter.replace('[name]', name)
    with open(f'Output/ReadyToSend/letter_to_{name}.txt', mode='w') as letter_to_name:
        letter_to_name.write(str(new_text))
