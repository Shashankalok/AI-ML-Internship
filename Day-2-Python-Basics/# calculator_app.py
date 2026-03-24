# calculator_app.py

import tkinter as tk

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Window
root = tk.Tk()
root.title("Calculator")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

row = 1
col = 0

for button in buttons:
    if button == "C":
        action = clear
    elif button == "=":
        action = calculate
    else:
        action = lambda x=button: click(x)

    tk.Button(root, text=button, width=5, height=2, command=action)\
        .grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()