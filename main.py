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

# link.get from string variable link