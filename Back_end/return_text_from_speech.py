'''
A significant portion of this script was taken from the following link:
https://www.assemblyai.com/blog/real-time-speech-recognition-with-python/
'''
import pyaudio
import re
import websockets
import asyncio
import base64
import json

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
 
# starts recording
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)

auth_key = '6e790915f96449ecbc21bafe22258ecf'
# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
async def send_receive(win):
    print(f'Connecting websocket to url ${URL}')
    # connect to websocket
    async with websockets.connect(
        URL,
        extra_headers=(("Authorization", auth_key),),
        ping_interval=5,
        ping_timeout=20
    ) as _ws:
        await asyncio.sleep(0.1)
        print("Receiving SessionBegins ...")
        session_begins = await _ws.recv()
        print(session_begins)
        print("Sending messages ...")
        async def send():
            # while the websocket is open, continuously convert data from microphone to text (via AssemblyAI)
            while _ws.open: 
                try:
                    data = stream.read(FRAMES_PER_BUFFER)
                    data = base64.b64encode(data).decode("utf-8")
                    json_data = json.dumps({"audio_data":str(data)})
                    await _ws.send(json_data)
                except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    break
                except Exception as e:
                    assert False, "Not a websocket 4008 error"
                await asyncio.sleep(0.01)
            
            return True
        
        async def receive(win):
            text_list = []
            puncs = ('.', '?', '!')
            end_recording = False
            # while websocket is open, continuously read data from the mic
            while _ws.open: 
                # get GUI window event (i.e. button click)
                events, values = win.read(timeout = 1)
                if events == "__RECORD__" or events == "__RECORD_POPUP__":
                    end_recording = True
                try:
                    # get transcribed text
                    result_str = await _ws.recv()
                    text_str = json.loads(result_str)['text']
                    print(text_str)
                    # only take a line once AssemblyAI punctuates it, to avoid repeats 
                    if text_str.endswith(puncs):
                        for sentence in re.split('\.|\?|!', text_str)[:-1]: # don't want last item of the list because its just a blank string after the final '.'
                            if sentence[0] == ' ': # if sentence starts with a space
                                sentence = sentence[1:]
                            # store the sentence in text_list
                            text_list.append(sentence + '.')
                    # if the 'end recording' button is hit, close the socket connection and return the list of sentences
                    if end_recording: 
                        await _ws.close()
                        return text_list
                except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                except Exception as e:
                    print(e)
                    assert False, "Not a websocket 4008 error"
        # continuously runs send() and receive()
        receive_res, text_list = await asyncio.gather(send(), receive(win))
        return text_list

def return_text(win):
    '''
    Returns a list of sentences, as punctuated by AssemblyAI.
    '''
    text_list = asyncio.run(send_receive(win))
    return text_list
    
