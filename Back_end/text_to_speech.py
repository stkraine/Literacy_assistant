from gtts import gTTS
from tempfile import TemporaryFile
import os
import pyglet
import time
import os

class incorrect_words():

    def __init__(self, word: str, index=0, file='temp_'):
        self.text = word
        self.index = index
        self.filename = file

    def _process_audio(self):
        self.filename = self.filename + self.text + ".mp3"
        self.gtts_obj = gTTS(self.text, lang='en', slow=False)
        self.gtts_obj.save(self.filename)

    def audio_playback(self):
        self._process_audio()
        playback = pyglet.media.load(self.filename, streaming=False)
        playback.play()

    def delete_temp_file(self):
        os.remove(self.filename)

def test():
    new_list = []
    temp_list = ["this", "is", "a", "test"]

    for word in temp_list:
        new_list.append(incorrect_words(word))

    for word in new_list:
        word.audio_playback()
        word.delete_temp_file()
        time.sleep(1)

        