from gtts import gTTS
from tempfile import TemporaryFile
import subprocess
import os
import pygame
import time


tts = gTTS(text='Hello World, nice to finally see you', lang='en')
filename = "hello.mp3"

def save_and_play():
	# Write to file 
	tts.save(filename)

	# Starting Sound
	print('Playing text output')
	status = subprocess.check_output("mpg321 ./" + filename, shell=True) 


def temp_and_play():
	f = TemporaryFile()
	tts.write_to_fp(f)

	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(f)
	pygame.mixer.music.play()
	time.sleep(5)
	f.close()

temp_and_play()
