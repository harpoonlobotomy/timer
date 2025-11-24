import FreeSimpleGUI as sg
import time
from math import floor

def counter_func(total_seconds):
    minutes = (floor(total_seconds / 60))
    sec = total_seconds - (minutes * 60)
    if len(str((round(sec)))) < 2:
        sec = "0" + str(round(sec))
    else:
        sec=round(sec)
    print(f" [[   {minutes}:{sec}]]")

    return str(minutes), str(sec)


def parse_inputtext(input_text:str):
    split_text=None
    minute = "00"
    sec = "00"
    separators = (":", ".", " ",)

    if len(input_text) > 2:
        #needs processing
        for x in separators:
            if x in input_text:
                split_text=input_text.split(x)
                print(f"Split text: {split_text}, len: {len(split_text)}, type: {type(split_text)}")

    if len(input_text) == 1:
        minute = input_text
    elif split_text and len(split_text) == 2:
            minute=split_text[0]
            sec = split_text[1]

    return minute, sec


def pause_toggle(paused): # paused is a bool, represents existing state, not desired state.




background_colour = "darkblue"
numbers_colour="yellow"
paused_numbers = background_colour

def counter_text(key_str="minutes", txt_col=numbers_colour):
    counting_font='Courier 40 bold'

    return sg.Text(text='00', key=key_str, size=(3,1), background_color=background_colour, relief="sunken", border_width=4, justification="center", font=counting_font, text_color=txt_col)

def make_button(width:float=10, height:float=10, key_str:str="Pause"):
        key_upper = key_str.upper()
        key_formatting = str("-" + key_upper + '-')
        print(key_formatting)
        return sg.Button(key_str, key=key_formatting, size=(10,10))

def make_window():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.

    numbers = [[counter_text("minutes"),
                counter_text("seconds"),
                  ]]

    column_one = [[
        sg.Column(layout=numbers, background_color="red")
    ]]
    column_two = [[sg.InputText(default_text="5:18", size=(16, 20), border_width=2, focus=False, enable_events=True, # focus=True, #turning this off so I can wipe the text when  you click it.
                                key='-INPUT-', tooltip="Input styles: \n     min.sec (15.10), \n     min:sec (15:10), \n     15m10s, \n     15m, \n     10s, \n     15 (defaults to minutes if not specified.)")
                   ],
                  [#sg.Stretch(),
                    make_button(width=5, height=5, key_str="Start"), make_button(width=5, height=5, key_str="Pause"), make_button(width=5, height=5, key_str="Exit")
                      #sg.Button('Start', key='-START-', size=(30,15)), sg.Button('Pause', key='-PAUSE-', size=(20,10)), ], [sg.Button('Exit', key='-EXIT-', size=(20,10)), sg.Stretch()],
                  ]
    ]


    main_contents = [
        [sg.Column(layout=column_one), sg.Column(layout=column_two)],
    ]

    layout = [[sg.Frame(title="clock", layout=main_contents)
               ]]

    # Create the Window
    minute = sec = 00
    running=False
    paused=False
    total_sec=10
    window = sg.Window('Window Title', layout, keep_on_top=True, finalize=True)
    window['-INPUT-'].bind("<Return>", "_Enter")
    while True:
        event, values = window.read(timeout=1000)
        if event == "-START-" or event == "-INPUT-" + "_Enter":
            if paused:
                pause_toggle(paused)
                paused=False
            input_text: str = values['-INPUT-']
            if input_text:
                print('You entered ', input_text)
                minute, sec = parse_inputtext(input_text)
                print(f"Minute: {minute}, sec: {sec}")
                print("Starting clock...")
                total_sec = (float(minute) * 60) + float(sec)

                window['minutes'].update(minute)
                window['seconds'].update(sec)
                running=True
                window['-START-'].update("[Restart]")
                # I really want to animate it opening its eyes when the timer's about to start.
            else:
                print("Please enter a number")

        if event == sg.WIN_CLOSED or event == '-EXIT-':  # if user closes window or clicks cancel
            running=False
            break

        if total_sec < 0:
            running = False

        if event == "-PAUSE-":
            if running:
                running = False
                window['-PAUSE-'].update("[Paused]")
                window['minutes'].update(text_color=paused_numbers)
                window['seconds'].update(text_color=paused_numbers)
                tog_on=False
                paused=True

            else:
                running = True
                window['-PAUSE-'].update("Pause")
                window['minutes'].update(text_color=numbers_colour)
                window['seconds'].update(text_color=numbers_colour)
                paused=False

        if paused:
            if tog_on:
                window['minutes'].update(text_color=paused_numbers)
                window['seconds'].update(text_color=paused_numbers)
                tog_on=False
            else:
                window['minutes'].update(text_color=numbers_colour)
                window['seconds'].update(text_color=numbers_colour)
                tog_on=True
            #window['seconds'].visible=False

        if running:
            minutes, seconds = counter_func(total_sec)
            window['minutes'].update(minutes)
            window['seconds'].update(seconds)
            print(f"min: {minutes}, sec: {seconds}")
            total_sec -= 1
            window.finalize()
            if total_sec < 0:
                running=False

    window.close()


if __name__ == '__main__':
    make_window()
