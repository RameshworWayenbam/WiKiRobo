from gtts import gTTS 
import pyglet
import time, os
import ConversationEngine

def tts(text,lang):
	file = gTTS(text = text, lang=lang)
	filename = "rameshwor.mp3"
	file.save(filename)

	music =pyglet.media.load(filename, streaming = False)
	music.play()

	time.sleep(music.duration)
	os.remove(filename)

def nerves(text,lang):
	text = ConversationEngine.brain(text)
	file = gTTS(text = text, lang=lang)
	filename = "rameshwor.mp3"
	file.save(filename)

	music =pyglet.media.load(filename, streaming = False)
	music.play()

	time.sleep(music.duration)
	os.remove(filename)

def vs(text,lang):
	speach =gTTS(text)
	speach.save("rameshwor.mp3")

def vtotext(text, lang):
	print(text)
	f = open("rameshwor.txt", "w")
	f.write(text)

def readfromfile(filename):
	text = ""
	with open(filename,"r") as file: 
		for line in file:
			text = text + line

	speach =gTTS(text)
	speach.save("rameshwor.mp3")