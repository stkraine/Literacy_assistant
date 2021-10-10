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

layout = [  [sg.Column([[sg.Text('This is the passage for you to read!')], 
            [sg.Multiline(default_text="Passage here",disabled=True, no_scrollbar=True)]]),sg.Column([[sg.Text('This is what you said!')],
            [sg.Multiline(disabled=True, no_scrollbar=True)]])],
            [sg.Button("Start Recording", key='__RECORD__'), sg.Cancel()]]

window = sg.Window("test_window", layout=layout)


# this function flips a buttons color, will be used to turn the recording button on, updates the flip variable
def flip_botton_color(id, flip):

    if not flip:
        flip = True
        window[id].update(button_color=("darkred","darkred"))

    else:
        flip = False
        window[id].update(button_color=("white","darkblue"))

    return flip




