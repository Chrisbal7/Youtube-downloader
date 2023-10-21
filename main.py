#! python3

import logging
from tkinter import ttk
import threading 
import pyperclip
import os
from pytube import YouTube



logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s - %(asctime)s')
logging.disable()

# todo set the default download directory to downloads if there is no configurations 
def set_download_dir():
    os.chdir(r'C:\Users\Admin\Downloads')
    

# This function return the percentage based on two numbers
def percent(tem, total):
    percentage = int((float(tem) / float(total)) * 100)
    return percentage


perc = ''


def progress_func(stream, _chunk, bytes_remaining):
    global perc
    print('\b' * len(perc), end='', flush=True)
    size = stream.filesize
    downloaded = size - bytes_remaining
    print(perc, end='')
    perc = str(percent(downloaded, size)) + ' % '


def download():
    yt = YouTube(link.get(), on_progress_callback=progress_func)
    download_check = yt.streams.filter(progressive=True, file_extension='mp4')\
        .order_by('resolution').desc().first().download()
    if download_check:
        print('Download completed', download_check)


root = Tk()
root.title('Video downloader')
root.geometry("600x400")
mainframe = ttk.Frame(root, padding='24 24 24 24')
img = PhotoImage(file='C:\\Users\\Admin\\Downloads\\youtube.png')
image = img.subsample(2, 2)
mainframe.grid(column=0, row=0)
link = StringVar()

ttk.Label(mainframe, text="Collez le lien et appuyer sur Download pour telecharger").grid(column=0, row=1, sticky='we')

ttk.Label(mainframe, image=image).grid(column=0, row=0)
link_entry = ttk.Entry(mainframe, textvariable=link)
link_entry.grid(column=0, row=2, sticky='we')
download_btn = ttk.Button(mainframe, text='Download', command=download)
download_btn.grid(column=0, row=3, sticky='w')

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.bind('<Return>', download)
root.mainloop()
