from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk
import PySimpleGUI as sg

"""
  DESIGN PATTERN 2 - Multi-read window. Reads and updates fields in a window
"""

sg.theme('Dark Grey 11')    # Add some color for fun

# 1- the layout
layout = [[sg.Text('How many documents will you merge?'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

# 2 - the window
window = sg.Window('FLUOstar data preprocessor', layout)

# 3 - the event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

        # In older code you'll find it written using FindElement or Element
        # window.FindElement('-OUTPUT-').Update(values['-IN-'])
        # A shortened version of this update can be written without the ".Update"
        # window['-OUTPUT-'](values['-IN-'])     

# 4 - the close
window.close()
