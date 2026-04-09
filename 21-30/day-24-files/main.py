with open('./Input/Letters/starting_letter.txt') as f:
  template = f.read()
with open('./Input/Names/invited_names.txt') as f:
  names = f.readlines()

for name in names:
  with open(f'./Output/letter_for_{name}.txt', mode='w') as f:
    letter = template.replace('[name]', name.strip())
    f.write(letter)