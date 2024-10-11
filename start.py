from input1 import take_input
from process1 import process
from output1 import output
from welcome import greet
from song import play_music_folder 
import os

os.system("cls")

greet()

while True:
    i = take_input()
    if i.lower() == 'temperature':
        import temperature
        temperature.temperature()
    elif i.lower() == 'play music':
        play_music_folder(r"D:\Music")
    else:
        o = process(i)
        output(o)
