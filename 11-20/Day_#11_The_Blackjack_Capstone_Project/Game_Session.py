from art import logo
from random import shuffle
from utils import cards
from Player import Player
from Dealer import Dealer

class GameSession(object):

  def __init__(self):
    self.player = Player()
    self.dealer = Dealer()
    self.deck = self.prepare_deck()
    self.keep_playing = True
    self.game_is_over = False
    self.deal_cards()
    
  def clear_game(self):
    self.deck = self.prepare_deck()
    self.player.reset()
    self.dealer.reset()
    self.deal_cards()

  def prepare_deck(self):
    deck = cards * 24
    shuffle(deck)
    return deck
  
  def show_winner(self):
    p = self.player.get_score()
    d = self.dealer.get_score()

    self.show_final_hands() 
    if p == d: 
      print("It's a draw!")
    elif d > 21 or p > d:
      print("You win!")
    else:
      print("You lose!")  
  
  def show_current_hands(self):
    print(f"\nYour cards: {self.player.get_hand()}, current score: {self.player.get_score()}")
    print(f"Computer's cards: {self.dealer.get_hand()}")

  def deal_cards(self):
    self.player.deal_hand(self.deck)
    self.dealer.deal_hand(self.deck)

  def show_final_hands(self):
    print(f"\nYour cards: {self.player.get_hand()}, your final score: {self.player.get_score()}")
    print(f"Computer's cards: {self.dealer.get_hand()}, computer's final score: {self.dealer.get_score()}")
  
  def start(self):
    print("\n" * 100)
    while(self.keep_playing):
      choice = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

      if choice != 'y':
        self.keep_playing = False
      else:
        print('\n' * 100)
        print(logo)
        keep_taking = True
        self.game_is_over = False

        # Start point
        while(keep_taking):
          score = self.player.calculate_hand()
          self.show_current_hands()
          choice = input("Type 'y' to get another card, type 'n' to pass: ")
          
          # Playes refuses to take another card
          if choice == 'n':
            keep_taking = False
          
          # Playes agrees to take another card
          else:
            self.player.take_card(self.deck)
            score = self.player.calculate_hand()

            # Game end check
            if score > 21:
              self.show_current_hands()
              print('You went over. You lose :C\n')
              keep_taking = False
              self.game_is_over = True
              self.clear_game()
          
        # Dealer's turn
        if not self.game_is_over:
          self.dealer.turn(self.deck)
          self.show_winner()
          self.clear_game()

            