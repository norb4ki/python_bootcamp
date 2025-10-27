from art import logo, vs
from game_data import data
import random

def compare_accounts (acc_a, acc_b, user_choice):
  """Takes two accounts to compare and the user choice (either 'a' or 'b').
  Checks which one has more followers. Returns True if user choice has more followers, False otherwise"""

  if acc_a["follower_count"] > acc_b["follower_count"]:
    return user_choice == 'a'
    
  elif acc_a["follower_count"] > acc_b["follower_count"]:
    return user_choice == 'b'

    
def show_current_pair (acc1, acc2):
  print(f"Compare A: {acc1["name"]}, a {acc1["description"]}, from {acc1["country"]}.")
  print(vs)
  print(f"Against B: {acc2["name"]}, a {acc2["description"]}, from {acc1["country"]}.")

def get_answer ():
  """Asks a user to input either 'A' or 'B'. Returns 'a' or 'b'"""
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  while answer != 'a' and answer != 'b':
    answer = input("Please, type 'A' or 'B': ").lower()
  return answer

def start():
  random.shuffle(data)
  game_is_over = False
  score = 0
  acc1 = data.pop()

  print(logo)
  while not game_is_over:
    acc2 = data.pop()
    show_current_pair(acc1, acc2)

    answer = get_answer()

    is_guess_right = compare_accounts(acc1, acc2, answer)
    if is_guess_right:
      score += 1
      acc1 = acc2
      print('\n' * 50)
      print(logo)
      print(f"You're right! Current score: {score}")
    else: 
      print(f"Sorry, that's wrong. Final score: {score}")
      game_is_over = True  

start()