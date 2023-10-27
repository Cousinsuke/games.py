
# hello_psg.py

import PySimpleGUI as psg

layout = [[psg.Text("Hello from PySimpleGUI")], [psg.Button("1")],[psg.Button("2")],[psg.Button("3")]]

# Create the window
window = psg.Window("Demo", layout, margins=(100, 50))
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == psg.WIN_CLOSED:
        break

window.close()