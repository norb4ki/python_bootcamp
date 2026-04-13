from turtle import Screen, Turtle
import pandas as pd
from constants.fodders import PROMPT_BASE, PROMPT_FAILED, PROMPT_REPEATED, TITLE_BASE
class GameSession():
  def __init__(self, map_path, data_path):

    self.game_is_over = False
    self.data = pd.read_csv(data_path)
    self.guessed = []
    self.total_amount = len(self.data)

    self.screen = Screen()
    self.screen.bgpic(map_path)

    self.prompt = PROMPT_BASE
    self.title = TITLE_BASE
    
    self.start()
    self.screen.mainloop()
  

  def start(self):
    while not self.game_is_over:
      self.take_attempt()
    self.handle_exit()
  
  def format_answer(self, answer):
    if type(answer) is not str:
      return None
    return answer.strip().title()
  
  def handle_answer(self, answer):
    if answer in self.guessed:
      self.prompt = PROMPT_REPEATED
    row = self.data[self.data.state == answer]
    if len(row) != 0:
      self.guessed.append(answer)
      self.title = f'{len(self.guessed)}/{self.total_amount} States Correct'
      x_coord = row.x.item()
      y_coord = row.y.item()
      self.draw_state(x_coord, y_coord, answer)
    else:
      self.prompt = PROMPT_FAILED


  def take_attempt(self):
    answer = self.screen.textinput(title=self.title, prompt=self.prompt)
    if answer == None:
      self.game_is_over = True
      return
    answer = self.format_answer(answer)
    self.handle_answer(answer)
  
  def draw_state(self, x_coord, y_coord, text):
    turtle = Turtle(visible=False)
    turtle.penup()
    turtle.teleport(x_coord, y_coord)
    turtle.write(text)
  
  def handle_exit(self):
    self.save_missed_states()
    self.screen.bye()

  def save_missed_states(self):
    states_list = self.data.state.to_list()
    missed_states = []
    for state in states_list:
      if state not in self.guessed:
        missed_states.append(state)

    pd.DataFrame(missed_states).to_csv('./data/states_to_learn.csv')
    