from gtts import gTTS
from tempfile import TemporaryFile
import os
import pyglet

import os

my_text =  ""
language = 'en'
accent = 'ca'
riley = gTTS(text=my_text, lang=language, slow=False)

filename = 'C:/tmp/temp.mp3'

riley.save(filename)

music = pyglet.media.load(filename, streaming=True)
music.play()

pyglet.app.run()

sleep(music.duration)
os.remove(filename)

class TextToSpeech():

    def __init__(self, transcript: list, lang='en'):
        self.text = transcript
        self.language = lang
        self.filename = "temp.mp3"
        self.gTTS_obj = gTTS(self.text, lang=self.language, slow=False)

    def audio_playback():
        pass

    def process_audio():
        pass


        




