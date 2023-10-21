import threading 
from pytube import YouTube

class Download:
    def __init__(self, link):
        self.link = link
        self.progress = "waiting"

    def download(self):
        yt = YouTube(self.link, on_progress_callback=self.progress)
        download_check = yt.streams.filter(progressive=True, file_extension='mp4')\
            .order_by('resolution').desc().first().download()
        return download_check
            
    
    def progress(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        downloaded = size - bytes_remaining
        progress = lambda: (downloaded // size) * 100 + ' % '
        self.update_progress(progress)

    def update_progress(self, progress):
        pass

class Queue:
    def __init__(self):
        self.frontier = []

