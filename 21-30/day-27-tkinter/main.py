import tkinter as tk

window = tk.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# my_label = tkinter.Label(text="I'm just a label", font=("Arial", 24, "bold"))
# my_label.grid(row=1, column=1)

# def handle_button_click():
#   my_label["text"] = input.get()
  

# button = tkinter.Button(text="Click it", command=handle_button_click)
# button.grid(row=2, column=2)

# new_button = tkinter.Button(text="Don't you dare clicking it", command=handle_button_click)
# new_button.grid(row=1, column=3)

# input = tkinter.Entry(width=10)
# input.grid(row=3, column=4)

#  + Entry + Label
mile_input = tk.Entry(width=10)
mile_input.insert(0, '0')
mile_input.grid(row=0, column=1)

miles_text = tk.Label(text="Miles", padx=10)
miles_text.grid(row=0, column=2)

#  Label + Label + Label
eq_text = tk.Label(text="is equal to", padx=10, pady=10)
eq_text.grid(row=1, column=0)

km_am_text = tk.Label(text="0")
km_am_text.grid(row=1, column=1)

km_text = tk.Label(text="Km")
km_text.grid(row=1, column=2)

def calc(miles):
  return int(miles) * 1.6

def handle_button_click():
  data = mile_input.get()
  km_am_text['text'] = calc(data)

#  + Button +
calc_button = tk.Button(text="Calculate", command=handle_button_click)
calc_button.grid(row=2, column=1)

window.mainloop()