import random
import hangman_words
import hangman_art

guessed_letters = []
chosen_word = random.choice(hangman_words.word_list)
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

# Game Start

print(hangman_art.logo)
while not game_over:
  print(hangman_art.stages[lives_left])
  print('Word to guess: ',placeholder)
  letter = guess_letter()

  if is_letter_valid(letter):
    guessed_letters.append(letter)
    
    if is_letter_in_word(letter):
      update_word(letter)
    else:
      lives_left -= 1
      print(f'****************************{lives_left}/6 LIVES LEFT****************************')

  if chosen_word == placeholder:
    print(f'The word is: {chosen_word}')
    print('***********************YOU WIN**********************\n')
    game_over = True
  
  if lives_left <= 0:
    print(hangman_art.stages[lives_left])
    print(f'The word is: {chosen_word}')
    print(f'***********************YOU LOSE**********************\n')
    game_over = True
    
