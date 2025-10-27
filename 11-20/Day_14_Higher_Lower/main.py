from art import logo, vs
from game_data import data
import random

def check_and_compare (first_person, second_person, user_choice):
  """Takes two persons to compare and the one the user chose.
  Checks which one has more followers. Returns True if user choice has more followers, False otherwise"""

  if first_person["follower_count"] > second_person["follower_count"]:
    if first_person["name"] == user_choice["name"]:
      return True
    else:
      return False
    
  elif second_person["follower_count"] > first_person["follower_count"]:
    if second_person["name"] == user_choice["name"]:
      return True
    else:
      return False
    
def show_current_pair (person1, person2):
  print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}.")
  print(vs)
  print(f"Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}.")

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
  first_item = data.pop()

  print(logo)
  while not game_is_over:
    second_item = data.pop()
    user_choice = {}
    show_current_pair(first_item, second_item)

    answer = get_answer()
    if answer == "a":
      user_choice = first_item
    else:
      user_choice = second_item    

    is_guess_right = check_and_compare(first_item, second_item, user_choice)
    if is_guess_right:
      score += 1
      first_item = second_item
      print('\n' * 50)
      print(logo)
      print(f"You're right! Current score: {score}")
    else: 
      print(f"Sorry, that's wrong. Final score: {score}")
      game_is_over = True  

start()