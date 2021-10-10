import PySimpleGUI as sg



theme = {'BACKGROUND': 'lightgray',
                'TEXT': 'black',
                'INPUT': 'white',
                'TEXT_INPUT': 'black',
                'SCROLL': 'white',
                'BUTTON': ('white', 'darkblue'),
                'PROGRESS': ('white', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('default_themes', theme)
sg.theme("default_themes")


def create_main_window():
    layout = [  [sg.Column([[sg.Text('Test passage')], 
            [sg.Multiline(default_text="The sky is blue",disabled=True, no_scrollbar=True)]]),sg.Column([[sg.Text('These are the words that you missed.')],
            [sg.Multiline(disabled=True, no_scrollbar=True, key="__OUTPUT__")]])],
            [sg.Button("Start Recording", key='__RECORD__'), sg.Cancel(key="__MAIN_CANCEL__")]]

    return sg.Window("test_window", layout=layout, finalize=True)


# this function flips a buttons color, will be used to turn the recording button on, updates the flip variable
def flip_botton_color(window, id, flip):

    if not flip:
        flip = True
        window[id].update(button_color=("darkred","darkred"))

    else:
        flip = False
        window[id].update(button_color=("white","darkblue"))

    return flip

# this function handles the pop-up for a word that was incorrectly updated.
def show_pop_up(failed_word):
    layout = [[sg.Text(failed_word)], [sg.Button("Play", key="__PLAY__")]]
    window = sg.Window(failed_word, layout, keep_on_top=True, finalize=True, size=(200,100))
    return window

#this function disables a button by key and window
def disable_button(window, key):
    window[key].update(disabled = True)
    
#this function enables a button by key and window
def enable_button(window, key):
    window[key].update(disabled = False)




