import pygame
import os
import time
import threading

pygame.init()
pygame.mixer.init()

folder_path = r"D:\Music" 

stop_event = threading.Event()
control_event = threading.Event()
finish_event = threading.Event()

def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()   

def stop_song():
    pygame.mixer.music.stop()
    stop_event.set()

def monitor_user_input():
    while not control_event.is_set():
        user_input = input("Enter 'next' to go to the next song, or 'stop' to stop the current song: ")
        if user_input.lower() == 'stop':
            stop_song()
            finish_event.set() 
        elif user_input.lower() == 'next':
            stop_song()
            control_event.set()
            break

def play_music_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            full_path = os.path.join(folder_path, filename)
            stop_event.clear()
            control_event.clear() 
            finish_event.clear()

            play_song(full_path)

            user_input_thread = threading.Thread(target=monitor_user_input)
            user_input_thread.start()

            while pygame.mixer.music.get_busy() and not control_event.is_set() and not finish_event.is_set():
                time.sleep(1)
            user_input_thread.join()
            if finish_event.is_set():
                break

    pygame.mixer.music.stop()
    finish_event.set()
