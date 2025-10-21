import random
word_list = ['pen', 'pineapple', 'apple', ]

guessed_letters = []
chosen_word = random.choice(word_list)
guessed_word = ''
for step in range (len(chosen_word)):
  guessed_word += '-'


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
    update_word()
  else:
    print('Wrong!\n')

def update_word():
  global guessed_word
  new_word = ''
  for letter in chosen_word:
    if letter in guessed_letters:
      new_word += letter
    else:
      new_word += '-'
  guessed_word = new_word

while not chosen_word == guessed_word:
  print('Word to guess: ',guessed_word)
  letter = guess_letter()

  if is_letter_valid(letter):
    guessed_letters.append(letter)
    is_letter_in_word(letter)
  