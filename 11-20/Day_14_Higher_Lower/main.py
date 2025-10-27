from art import logo, vs
from game_data import data
import random

def check_and_compare (acc1, acc2, user_choice):
  """Takes two accounts to compare and the one the user chose.
  Checks which one has more followers. Returns True if user choice has more followers, False otherwise"""

  if acc1["follower_count"] > acc2["follower_count"]:
    if acc1["name"] == user_choice["name"]:
      return True
    else:
      return False
    
  elif acc2["follower_count"] > acc1["follower_count"]:
    if acc2["name"] == user_choice["name"]:
      return True
    else:
      return False
    
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
    user_choice = {}
    show_current_pair(acc1, acc2)

    answer = get_answer()
    if answer == "a":
      user_choice = acc1
    else:
      user_choice = acc2    

    is_guess_right = check_and_compare(acc1, acc2, user_choice)
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