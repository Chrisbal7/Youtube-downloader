#! python3

import tkinter as tk

root = tk.Tk()
btn = tk.Button(root, text="Download")
btn.config(command=lambda: print('Hello, Chris'))
btn.pack(padx=200, pady=300)
root.title('Download YT Video')
root.mainloop()