#!usr/bin/python3

import tkinter as tk

BACKGROUND = ""
FOREGROUND = ""



"""Function that create a button on the layout"""
def get_button(row, col):  
    button = tk.Button(background=BACKGROUND,
                       foreground=FOREGROUND)
    button.grid(row=row, column=col)
    return button


def label(row, col, text):
    label = tk.Label(background=BACKGROUND,
                       foreground=FOREGROUND,
                       text=text)
    label.grid(row=row, column=col)
    return label


window = tk.Tk()
window.title("uMate")
# Create an icon for the app, when running
logo = tk.PhotoImage(file="images/logo.png")
window.iconphot(logo)

window.mainloop()
