import PySimpleGUI as sg
from utils import get_meaning, get_synonyms, get_antonyms

greeting = "Hi, I am a word bot. I can help you with words\n"

layout = [
    [sg.Multiline(greeting, font=("Arial", 14), size=(70, 15), key='output')],
    [sg.InputText("", font=("Arial", 14), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Arial", 14), bind_return_key=True, key='meaning'),
     sg.Button("Synonyms", font=("Arial", 14), key='synonym'),
     sg.Button("Antonyms", font=("Arial", 14), key='antonym'),
     sg.Button("Clear", font=("Arial", 14), key='clear')
    ]
]

def display_meaning(word):
    meaning = get_meaning(word)
    window['output'].print("WORD: " + word)
    if meaning:
        window['output'].print("MEANING: ", meaning)
    else:
        display_error("Word is not found in corpus")

def display_synonym(word):
    synonym = get_synonyms(word)
    window['output'].print("SYNONYM: ", synonym)

def display_error(message):
    window['output'].print("ERROR: " + message, text_color='red')


if __name__ == '__main__':
    window = sg.Window('File Explorer', layout)

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'meaning':
            display_meaning(values['input'])
        elif event == 'synonyms':
            display_synonym(values['input'])
    window.Close()