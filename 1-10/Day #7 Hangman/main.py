import random
word_list = ['pen', 'pineapple', 'apple', ]
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

guessed_letters = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
lives_left = 6
placeholder = ''
for step in range (len(chosen_word)):
  placeholder += '-'


def guess_letter():
  return input('Guess a letter: ').lower()

def is_letter_valid(letter):
  if len(letter) != 1:
    print('You should type only one letter\n')
    return False
  elif letter.upper() == letter.lower():
    print('Numbers and characters are prohibited\n')
    return False
  elif letter in guessed_letters:
    print('You guessed this letter before\n')
    return False
  else:
    return True
  
def is_letter_in_word(letter):
  if letter in chosen_word:
    print('Right!\n')
    return True
  else:
    print('Wrong!\n')
    return False

def update_word(letter):
  global placeholder
  new_word = ''

  for letter in chosen_word:
    if letter in guessed_letters:
      new_word += letter
    else:
      new_word += '-'
  placeholder = new_word

while not game_over:
  print(stages[lives_left])
  print('Word to guess: ',placeholder)
  letter = guess_letter()

  if is_letter_valid(letter):
    guessed_letters.append(letter)
    
    if is_letter_in_word(letter):
      update_word(letter)
    else:
      lives_left -= 1
      print(f'You have {lives_left} lives left\n')

  if chosen_word == placeholder:
    print('You won!\n' \
    f'The word is: {chosen_word}')
    game_over = True
  
  if lives_left <= 0:
    print(stages[lives_left])
    print('You lose :(\n' \
    f'The word is: {chosen_word}')
    game_over = True
    
