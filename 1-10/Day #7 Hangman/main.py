import random
word_list = ['pen', 'pineapple', 'apple', ]

guessed_letters = []
chosen_word_list = random.choice(word_list).split()
guessed_word_list = []
for step in range (len(chosen_word_list)):
  guessed_word_list.append('_')


def guess_letter():
  return input('Guess a letter: ').lower()

def is_letter_valid(letter):
  if len(not letter == 1):
    print('You should type only one letter')
    return False
  elif letter.upper() == letter.lower():
    print('Numbers and characters are prohibited')
    return False
  elif letter in guessed_letters:
    print('You guessed this letter before')
    return False
  else:
    return True
  
def is_letter_in_word(letter):
  if letter in chosen_word:
    print('Right!')
    update_word()
  else:
    print('Wrong!')

def update_word():
  print('To do')

while not chosen_word == word_to_print:
  print('Word to guess: ',word_to_print)
  letter = guess_letter()
  is_letter_in_word(letter)
  