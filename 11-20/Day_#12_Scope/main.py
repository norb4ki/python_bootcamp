from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
user_guess = 0
guesses_left = 0
game_over = False

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while difficulty!= 'easy' and difficulty!= 'hard':
  difficulty = input("You can choose only from 'easy' and 'hard': ").lower()

if difficulty == "easy":
  guesses_left = 10
else:
  guesses_left = 5

while not game_over and guesses_left > 0:
  print(f"You have {guesses_left} attempts to guess the number.")
  guess = int(input("Take a guess: "))
  guesses_left -= 1

  if guess > secret_number:
    print("Too high.")
  elif guess < secret_number:
    print("Too low.")
  else:
    game_over = True
    print('You guessed correctly!')
  
  if guesses_left <= 0 and not game_over:
    print('You are out of guesses. You lose!')
    game_over = True