from tkinter import END, EW, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project



def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  let = [choice(letters) for _ in range(randint(8, 10))]
  num = [choice(numbers) for _ in range(randint(2, 4))]
  sym = [choice(symbols) for _ in range(randint(2, 4))]

  password_list = let + num + sym
  shuffle(password_list)
  return ''.join(password_list)

def handle_generate_button():
  password = generate_password()
  password_input.delete(0, END)
  password_input.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def handle_add_button():
  data = get_form_data()
  resp = validate_data(data)
  if resp:
    is_ok = messagebox.askokcancel(title=data["website"], message=f'These are your credentials: \nEmail: {data["username"]}\nPassword: {data["password"]}\nContinue saving?')
    if is_ok: 
      save_data(data["to_string"])
      clear_form()
  else:
    messagebox.showerror(title='Error', message="You forgot to fill some fields")


def get_form_data():
  website = website_input.get()
  username = username_input.get()
  password = password_input.get()
  return {
    "website": website, 
    "username": username, 
    "password": password,
    "to_string": f'{website} | {username} | {password}'
  }

def validate_data(data) -> bool:
  if len(data["website"]) == 0:
    return False
  if len(data["username"]) == 0:
    return False
  if len(data["password"]) == 0:
    return False
  return True


def save_data(data):
  with open('./credentials.txt', mode='a') as f:
    f.write(data)


def clear_form():
  website_input.delete(0, END)
  password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0, sticky=EW)

# Website row
website_label = Label(text='Website:')
website_label.grid(row=1, column=0, sticky=EW)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky=EW)

# email row
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0, sticky=EW)
username_input = Entry(width=35)
username_input.insert(0, 'user@template.com')
username_input.grid(row=2, column=1, columnspan=2, sticky=EW)

# pass row
password_label = Label(text='Password', )
password_label.grid(row=3, column=0, sticky=EW)
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=EW)
password_btn = Button(text='Generate Password', command=handle_generate_button)
password_btn.grid(column=2, row=3, sticky=EW)

# add button row
add_btn = Button(text="Add", width=36, command=handle_add_button)
add_btn.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()