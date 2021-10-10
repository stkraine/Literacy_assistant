import pyaudio
 
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

# ---------------------------------------------------

import websockets
import asyncio
import base64
import json
# from configure import auth_key
auth_key = '6e790915f96449ecbc21bafe22258ecf'
# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
text_list = []
async def send_receive():
    print(f'Connecting websocket to url ${URL}')
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
        
        async def receive():
            while _ws.open: # while _ws.is_open()?
                try:
                    result_str = await _ws.recv()
                    text_str = json.loads(result_str)['text']
                    print(text_str)  
                    if text_str.endswith('.'):
                        text_list.append(text_str)
                        if len(text_list) > 6:
                            await _ws.close()
                            return text_list
                    # print('text_list:', text_list)
                except websockets.exceptions.ConnectionClosedError as e:
                    print(e)
                    assert e.code == 4008
                    # break
                except Exception as e:
                    print(e)
                    assert False, "Not a websocket 4008 error"
        text_list = []
        receive_res, text_list = await asyncio.gather(send(), receive())
        return text_list
        # text_list = await asyncio.get_event_loop().run_until_complete(send(), receive())
        # return send_result, receive_result

def return_text():
    '''
    Returns a list of sentences, as punctuated by AssemblyAI
    '''
    text_list = asyncio.run(send_receive())
    return text_list
    