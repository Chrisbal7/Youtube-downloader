#! python3

import logging
from pytube import YouTube
import sys
import os

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s - %(asctime)s')
logging.disable()

link = ''

os.chdir(r'C:\Users\Admin\Downloads')

if len(sys.argv) > 1:
    link = sys.argv[1]
    yt = YouTube(link)
    yt.streams.first().download()

