import math
from pydoc import text
from tkinter import Button, Label, PhotoImage, Tk, Canvas

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
checkmark_text = ''
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global checkmark_text, reps
  if timer:
    window.after_cancel(timer)
    checkmark_text = ''
    reps = 0
    title.config(text="Timer", fg=GREEN)
    checkmark_label.config(text=checkmark_text)
    canvas.itemconfig(timer_txt, text='00:00')

    # title = Label(text="Timer", font=("Arial", 30, 'bold'), fg=GREEN, bg=YELLOW)



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def get_timer_period():
  global reps
  if reps % 2 == 1:
    title.config(text="Work", fg=GREEN)
    return WORK_MIN * 60
  if reps % 8 == 0:
    title.config(text="Long Break", fg=RED)
    return LONG_BREAK_MIN * 60
  title.config(text="Short Break", fg=PINK)
  return SHORT_BREAK_MIN * 60

def handle_start():
  period = get_timer_period()
  count_down(period)

def time_to_text(seconds: int):
  mins = math.floor(seconds / 60)
  secs = seconds % 60

  zero_prefix = ''
  if secs < 10:
    zero_prefix = '0'

  return f'{mins}:{zero_prefix}{secs}'

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds):
  global reps, checkmark_text, timer
  text = time_to_text(seconds)
  canvas.itemconfig(timer_txt, text=text)
  if seconds > 0:
    timer = window.after(1, count_down, seconds-1)
  else: 
    reps += 1
    if reps % 2 == 0:
      checkmark_text = f'{checkmark_text}✓'
      checkmark_label.config(text=checkmark_text)
    handle_start()
  
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

title = Label(text="Timer", font=("Arial", 30, 'bold'), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(103, 130, text='00:00', fill="white", font=('Arial', 20, 'bold'))
canvas.grid(column=1, row=1)

start_btn = Button(text="start", padx=10, pady=10, command=handle_start)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", padx=10, pady=10, command=reset_timer)
reset_btn.grid(column=2, row=2)

checkmark_label = Label(text=checkmark_text, fg=GREEN, font=("Courier", 24, "bold"), bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# count_down(5)

window.mainloop()