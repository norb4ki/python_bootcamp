from GameSession import GameSession

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.bgpic(image)


# answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
# turtle.mainloop()
game = GameSession("./assets/blank_states_img.gif", "./data/50_states.csv")