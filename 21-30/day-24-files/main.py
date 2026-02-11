with open('./Input/Names/invited_names.txt', "r") as f:
  template = open('./Input/Letters/starting_letter.txt', "r").read()
  guest_list = f.readlines()
  for line in guest_list:
    name = line.split()[0]
    letter = template.replace('[name]', name)
    file = open(f'./Output/ReadyToSend/{name}.txt', "w")
    file.write(letter)
    file.close()