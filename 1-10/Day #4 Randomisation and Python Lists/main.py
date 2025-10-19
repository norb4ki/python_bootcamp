import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ascii_arts = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
if user_choice < 0 or user_choice > 2:
    print('Wrong choice, out of boundaries')
else:
    print(ascii_arts[user_choice])
    print(f'Computer chose:\n{ascii_arts[computer_choice]}')
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice - computer_choice == 1 or user_choice - computer_choice == -2:
        print('You won!')
    else:
        print('You lose')
        