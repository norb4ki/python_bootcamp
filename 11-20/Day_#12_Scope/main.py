from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def is_answer_correct(guess, answer):
  """Returns True is the guess was correct, False otherwise """
  if guess > answer:
    print("Too high.")
    return False
  elif guess < answer:
    print("Too low.")
    return False
  else:
    print(f'You got it! The answer is {answer}.')
    return True

def get_difficulty():
  """Asks a user for a difficulty and returns corresponding amount of turns"""
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  while difficulty!= 'easy' and difficulty!= 'hard':
    difficulty = input("You can choose only from 'easy' and 'hard': ").lower()

  if difficulty == "easy":
    turns = EASY_LEVEL_TURNS
  else:
    turns = HARD_LEVEL_TURNS
  return turns


print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
turns = get_difficulty()
game_over = False

while turns > 0:
  print(f"You have {turns} attempts to guess the number.")
  guess = int(input("Take a guess: "))
  turns -= 1

  if(is_answer_correct(guess, answer)):
    break
  
  if turns <= 0 and not game_over:
    print('You are out of guesses. You lose!')
    break