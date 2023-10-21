#!usr/bin/python3

import tkinter as tk


blue = "#5490f2"
white = "#F0EFF0"
red = "D7222C"

BACKGROUND = white
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
umate_img = tk.PhotoImage(file="images/logo.png")
logo= umate_img.subsample(1, 1)
window.wm_iconphoto(True, logo)


# Create frames
download_frame = tk.Frame(window, background=BACKGROUND)
download_frame.grid(row=0, column=0)

files_frame = tk.Frame(window, background=BACKGROUND)
files_frame.grid(row=0, column=1)

window.mainloop()
