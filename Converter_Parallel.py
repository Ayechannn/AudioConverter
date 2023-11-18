import moviepy.editor
from tkinter import filedialog 
import time
import multiprocessing


aud_name = ["Gemini_Know_me.mp3","Why_don't_U_Stay.mp3","Chinese.mp3","2_baddies.mp3"]

vid = ["Gemini_Know_me.mp4","Why_don't_U_Stay.mp4","Chinese.mp4","2_baddies.mp4"]

def converter(vid,aud_name):
    video = moviepy.editor.VideoFileClip(vid)
    audio = video.audio
    audio.write_audiofile(aud_name)

if __name__=="__main__":
    start = time.time()
    processes = []

    for i,j in zip(vid, aud_name):
        p= multiprocessing.Process(target=converter(i,j))
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(f'Total Time Taken is {round(end-start,2)} second(s)')