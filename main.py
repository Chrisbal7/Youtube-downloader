#! python3

import logging
from pytube import YouTube
from pytube.cli import on_progress
import os
import time

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s - %(asctime)s')
logging.disable()

os.chdir(r'C:\Users\Admin\Downloads')
link = input('Paste the link here, Click ENTER to download\n')


def percent(tem, total):
    percentage = ((float(tem) / float(total)) * 100)
    return int(percentage)


perc = ''


def progress_func(stream, _chunk, bytes_remaining):
    global perc
    print('\b' * len(perc), end='', flush=True)
    size = stream.filesize
    downloaded = size - bytes_remaining
    print(perc, end='')
    perc = str(percent(downloaded, size)) + ' % '


yt = YouTube(link, on_progress_callback=progress_func)
download_check = yt.streams.filter(progressive=True, file_extension='mp4')\
    .order_by('resolution').desc().first().download()
if download_check:
    print('Download completed', download_check)
