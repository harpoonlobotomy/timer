## basic timer, prints time to terminal. Cannot be interacted with while running as it runs inline.
# - harpoon, 22/11/25

import time
from math import floor
import FreeSimpleGUI as sg


def start_clock(input_text: str):
    if "." in input_text:
        minutes, seconds = input_text.split(".")
        seconds = (float(minutes) * 60) + float(seconds)
    else:
        seconds = float(input_text) * 60
    min_set = seconds

    while min_set > 0:
        minutes = floor(min_set / 60)
        seconds = min_set - (minutes * 60)
        if len(str((round(seconds)))) < 2:
            seconds = "0" + str(round(seconds))
            print(f" [[   {minutes}:{seconds}]]")
        else:
            print(f" [[   {minutes}:{round(seconds)}]]")

        time.sleep(1)  # every second
        min_set -= 1  # take one second


def make_window():
    input_text = None
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    column_one = [[sg.Text('Enter something on Row 2'), sg.InputText(default_text='', size=(50, 20), border_width=2,
                                                                     focus=True, key='-INPUT-'
                                                                     )
                   ],
                  [sg.Button('Submit', key='-SUBMIT-'), sg.Button('Cancel')],
                  ]

    layout = [[sg.Column(layout=column_one, size=(400, 200), justification='center',
                         key='layout'
                         )
               ]
              ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        if event == "-SUBMIT-":
            input_text: str = values['-INPUT-']
            if input_text:
                print('You entered ', input_text)
                try:
                    input_text = input_text.strip()
                    print("Starting clock...")
                    start_clock(input_text)
                except ValueError:
                    print("Please enter a number")

            else:
                print("Please enter a number")

        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

    window.close()


if __name__ == '__main__':
    make_window()
