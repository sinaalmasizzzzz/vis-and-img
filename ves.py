from moviepy import editor
import threading

def seda1(url):
    video = editor.VideoFileClip(url)
    video.audio.write_audiofile(f"1.mp3")


def seda2(url):
    video = editor.VideoFileClip(url)
    video.audio.write_audiofile(f"2.mp3")

def seda3(url):
    video = editor.VideoFileClip(url)
    video.audio.write_audiofile(f"3.mp3")

def seda4(url):
    video = editor.VideoFileClip(url)
    video.audio.write_audiofile(f"4.mp3")

def seda5(url):
    video = editor.VideoFileClip(url)
    video.audio.write_audiofile(f"5.mp3")



t1=threading.Thread(target=seda1,args=["1.mp4"])
t2=threading.Thread(target=seda2,args=["2.mp4"])
t3=threading.Thread(target=seda3,args=["3.mp4"])
t4=threading.Thread(target=seda4,args=["4.mp4"])
t5=threading.Thread(target=seda5,args=["5.mp4"])


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()