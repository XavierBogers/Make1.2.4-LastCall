# Script for GUI for easier use

import PySimpleGUI as gui

# creation of button for the use of external functions
layout = [[gui.Text("Hello Human User")], [gui.Button("Test Button")], [gui.Button("IP Display")], [gui.Button("Password Generator")],
          [gui.Button("System Update")], [gui.Button("System info")], [gui.Button("Network or Port Scanner")], [gui.Button("GPIO Display & Status")],
          [gui.Button("Software Install")]]

window = gui.Window("Shenanigans", layout, margins=(400,200))

# Window closes when the 'Test Button' is pushed
while True:
    event, values = window.read()
    if event == "Test Button" or event == gui.WIN_CLOSED:
        break

window.close()