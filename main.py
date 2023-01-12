#! python3

import logging
import pytube
from pytube import YouTube
import sys
import os

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s - %(asctime)s')
# logging.disable()

link = ''

os.chdir(r'C:\Users\Admin\Downloads')

if len(sys.argv) > 1:
    link = sys.argv[1]
    yt = YouTube(link)
    download_check = yt.streams.filter(progressive=True, file_extension='mp4')\
        .order_by('resolution').desc().first().download()
    if download_check:
        print('Download completed', download_check)

