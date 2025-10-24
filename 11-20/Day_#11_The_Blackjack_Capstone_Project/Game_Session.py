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
    self.deal_cards()
    
  def clear_game(self):
    self.deck = self.prepare_deck()
    self.player.reset()
    self.dealer.reset()

  def prepare_deck(self):
    deck = cards * 24
    shuffle(deck)
    return deck
  
  def show_current_hands(self):
    print(f"\nYour cards: {self.player.get_hand()}, current score: {self.player.get_score()}")
    print(f"Computer's cards: {self.dealer.get_card()}\n")

  def deal_cards(self):
    self.player.deal_hand(self.deck)
    self.dealer.deal_hand(self.deck)
    
  
  def start(self):
    while(self.keep_playing):
      choice = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

      if choice != 'y':
        self.keep_playing = False

      else:
        print('\n' * 20)
        print(logo)
        keep_taking = True

        while(keep_taking):
          score = self.player.calculate_hand()
          self.show_current_hands()
          choice = input("Type 'y' to get another card, type 'n' to pass: ")

          if choice == 'n':
            keep_taking = False
          else:
            self.player.take_card(self.deck)
            score = self.player.calculate_hand()

            if score > 21:
              self.show_current_hands()
              print('You went over. You lose :C\n')
              keep_taking = False
            elif score == 21:
              self.show_current_hands()
              print('You win with a black jack!\n')
              keep_taking = False
            