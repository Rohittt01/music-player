from pygame import mixer
import tkinter

songs_directory = "./songs"
root = tkinter.Tk()
root.geometry("400x300")
root.title("Music Player")
import os
file_dir = './songs'
file_path = [file for file in os.listdir(file_dir) if file.endswith(".mp3")]
mixer.init()
i = 0

def play_music():
    mixer.music.load(filename=f"songs/{file_path[i]}")
    mixer.music.play() 

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()
def next_song():
    global i
    i += 1
    if i >= len(file_path):
        i = 0
    mixer.music.load(filename=f"songs/{file_path[i]}")
    mixer.music.play()


play_button = tkinter.Button(root, text="Play", command=play_music)
stop_button = tkinter.Button(root, text="Stop", command=stop_music)
pause_button = tkinter.Button(root, text="Pause", command=pause_music)
unpause_button = tkinter.Button(root, text="Unpause", command=unpause_music)
next_button = tkinter.Button(root, text="Next", command=next_song)
play_button.pack()
stop_button.pack()
pause_button.pack()
unpause_button.pack()
next_button.pack()
root.mainloop()



