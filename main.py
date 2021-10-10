from Front_end.User_interface import *
from config import *


def main():
    RECORDING = False

    window1 = create_main_window()

    open_windows = [window1]

    while(True):
        window, event, values = sg.read_all_windows(timeout=1)

        # checks if the start recording button has been pressed
        if "__RECORD__" == event:
            RECORDING = flip_botton_color(window, "__RECORD__", RECORDING)
            disable_button(window, "__RECORD__")
            disable_button(window, "__MAIN_CANCEL__")
            temp_win = show_pop_up("Test")

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
