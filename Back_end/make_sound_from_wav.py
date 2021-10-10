# -*- coding: <utf-8> -*-
import pyaudio
import wave
import time
import sys
import sounddevice as sd
import numpy as np

args = ['test.py', 'Recording.wav']

if len(args) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % args[0])
    sys.exit(-1)

wf = wave.open(args[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

# start the stream (4)
stream.start_stream()

# wait for stream to finish (5)
while stream.is_active():
    time.sleep(0.1)

CHUNKSIZE = 1024

# stop stream (6)
stream.stop_stream()
data = [0]
while len(data) != 0:
    data = stream.read(CHUNKSIZE)
    numpydata = np.frombuffer(data, dtype=np.int16)
    sd.play(numpydata)

stream.close()
wf.close()

# close PyAudio (7)
p.terminate()