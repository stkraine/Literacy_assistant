from Front_end.User_interface import *
from config import *

RECORDING = False

while(True):
    event, values = window.read(timeout=1)


    if "__RECORD__" == event:
        RECORDING = flip_botton_color("__RECORD__", RECORDING)

    
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
        

window.close()
