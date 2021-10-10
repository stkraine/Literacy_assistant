from Front_end.User_interface import *
from config import *
from Back_end.return_text_from_speech import *
from Back_end.text_to_speech import *


def main():
    RECORDING = False

    window1 = create_main_window()

    open_windows = [window1]

    test_string = ""

    while(True):
        window, event, values = sg.read_all_windows(timeout=1)

        # checks if the start recording button has been pressed
        if "__RECORD__" == event and not RECORDING:
            RECORDING = flip_botton_color(window, "__RECORD__", RECORDING)
            output = return_text(window1)
            for sentence in output:
                test_string = test_string + sentence
            
            window1["__OUTPUT__"].update(test_string)
            # disable_button(window, "__RECORD__")
            # disable_button(window, "__MAIN_CANCEL__")
        if "__RECORD__" == event and RECORDING:
            RECORDING = flip_botton_color(window, "__RECORD__", RECORDING)
            word = incorrect_words(window1["__OUTPUT__"].get())
            word.audio_playback()
            word.delete_temp_file()
            
            #temp_win = show_pop_up("Test")

        # checks if the window is to be closed, basically ends the program
        # closes all other open windows
        if event in (sg.WIN_CLOSED, '__MAIN_CANCEL__') and window == window1:
            for win in open_windows:
                win.close()
            break

        if event in (sg.WIN_CLOSED, 'Cancel') and window != window1:
            window.close()

            # check if the only window open is the main window
            # if yes: enable all buttons again
            if len(open_windows) == 1:
                enable_button(window1, "__RECORD__")
                enable_button(window1, "__MAIN_CANCEL__")
            

if __name__ == '__main__':
    main()
